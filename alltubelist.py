import random, time, math, sys, pygame

pygame.init()
fp = open('pyprowords.txt', 'r')
wordlist = []
for line in fp:
    wordlist.append(line.strip())


def printimage(image):
    display.blit(image.frog, (image.x, image.y))


def printText(msg, color='BLACK', pos=(0, 512), infon=0):
    textSurface = font[infon].render(msg, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    display.blit(textSurface, textRect)


White = (255, 255, 255)
wid = 800
hei = 512 + 50
font = [pygame.font.SysFont("consolas", 20),
        pygame.font.SysFont("consolas", 18),
        pygame.font.SysFont("consolas", 16),
        pygame.font.SysFont("consolas", 30),
        pygame.font.SysFont("나눔고딕", 50),
        pygame.font.SysFont("나눔고딕", 16)]
display = pygame.display.set_mode((wid, hei))
display.fill(White)
pygame.display.set_caption("해상구조 SOS")
texty = ""
input_word = ""
pressed_button = list()
vel_plus = 0.2
vel_tube = 0.2

# 나와 컴퓨터의 튜브가 빠지는 시간간격
delta_t_pop = [7, 7]
start_time_pop = [time.time(), time.time()]

# 컴퓨터가 튜브를 먹는 시간간격
en_delta_t = 4
en_start_time = time.time()


class item:
    def __init__(self, inputx, inputy, w=80, h=80):
        self.itemnum = random.randrange(0, 7) + 1
        self.imagename = "pyproimage/image" + (str)(self.itemnum) + ".png"
        self.frog = pygame.image.load(self.imagename)  # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w, h))
        self.x = inputx
        self.y = inputy
        self.word = random.choice(wordlist)


class Tube:
    def __init__(self, inputx, inputy, w=240, h=100):
        self.imagename = "pyproimage/tubevector.png"
        self.frog = pygame.image.load(self.imagename)  # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w, h))
        self.x = inputx
        self.y = inputy
        self.word = random.choice(wordlist)


class Charac:
    def __init__(self, inputx, inputy, w=100, h=100):
        self.charnum = random.randrange(1, 3) + 1
        self.imagename = "pyproimage/char" + (str)(self.charnum) + ".png"
        self.frog = pygame.image.load(self.imagename)  # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w, h))
        self.x = inputx
        self.y = inputy


class Otherimage:
    def __init__(self, inputx, inputy, w, h, imaname):
        self.imagename = imaname
        self.frog = pygame.image.load(self.imagename)  # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w, h))
        self.x = inputx
        self.y = inputy


wallpaper = Otherimage(0, 212, 800, 300, "pyproimage/wallpaper.png")
boom = Otherimage(-50, 100, 100, 100, "pyproimage/boom.png")

item1 = item(800, 100)
char_tube_word = [random.choice(wordlist), random.choice(wordlist)]
pause_image = Otherimage(750, 0, 50, 50, "pyproimage/Pause.png")
pause_im1 = Otherimage(-40, -150, wid + 60, hei, "pyproimage/rule.png")
play_image = Otherimage(750, 0, 50, 50, "pyproimage/Play.png")

# char1,2는 각각 나와 컴퓨터의 캐릭터이며, x와 y좌표를 인자로 받는다.
char1 = Charac(200, 270)
char2 = Charac(570, 270)
charlist = [char1, char2]
tube_under_list = []

iteminfo=[]
for i in range(7):
    if (i+1)<3:
        iteminfo.append(Otherimage(40+122*i, 270, 100, 100, "pyproimage/image"+(str)(i+1)+".png"))
    if (i+1)>3:
        iteminfo.append(Otherimage(40+122*(i-1), 270, 100, 100, "pyproimage/image"+(str)(i+1)+".png"))
iteminfo.append(Otherimage(37,232,300,24,"pyproimage/iteminfo1.png"))

informate=[]
for i in range(6):
    informate.append(Otherimage(40,390,570,115,"pyproimage/inform"+(str)(i+1)+".png"))

boxes=[]
for i in range(6):
    boxes.append(Otherimage(40+122*i, 270, 100, 100, "pyproimage/box.png"))
boxflag=-1

def check_use(word):
    while True:
        changed = True
        if word == item1.word:
            word = random.choice(wordlist)
            continue
        for j in tube_under_list:
            if j.word == word:
                word = random.choice(wordlist)
                changed = False
                break
        for j in char_tube_word:
            if j == word:
                word = random.choice(wordlist)
                changed = False
                break
        if changed:
            break
    return word


# 단어가 적혀있는 튜브들의 리스트

for i in range(4):
    temp = Tube(200 * i, 400)
    temp.word = check_use(temp.word)
    tube_under_list.append(temp)

# 나와 컴퓨터의 튜브 리스트이다.
# tube_upper_list[0] 리스트에는 내 튜브 인스턴스가,
# tube_upper_list[1] 리스트에는 상대 튜브 인스턴스가 들어있다.
tube_upper_list = [[], []]
flag = False
score = 0
pause_image = Otherimage(750, 0, 50, 50, "pyproimage/Pause.png")
itemvel = 2
sinx = [0, 0.8]
rep = False
is_start = True
lev = 1
is_level_up = time.time() - 1
is_unbeatable = [time.time() - 3, time.time() - 3]
is_freeze = [time.time() - 2, time.time() - 2]
is_confuse = [time.time() - 3, time.time() - 3]
com_move = 0


def shiver():
    global tube_upper_list
    global sinx
    for i in range(2):
        for tubes in tube_upper_list[i]:
            tubes.y += 0.5 * math.sin(sinx[i])
            tubes.x += 0.2 * math.sin(sinx[i] * 2)
        charlist[i].y += 0.5 * math.sin(sinx[i])
        charlist[i].x += 0.2 * math.sin(sinx[i] * 2)
    item1.y += 0.3 * math.sin(sinx[i])
    for tubes in tube_under_list:
        tubes.y += 0.15 * math.sin(sinx[i])
    for i in range(2): sinx[i] += 0.04


# more이 0(tube_upper_list의 index!)이면 내 쪽에, 1이면 상대쪽에 튜브를 쌓는 함수
def stacktube(more):
    xlist = [130, 500]
    if len(tube_upper_list[more]) == 0:
        new_player_tube = Tube(xlist[more], 300)
    else:
        new_player_tube = Tube(xlist[more], tube_upper_list[more][len(tube_upper_list[more]) - 1].y - 30)
    tube_upper_list[more].append(new_player_tube)
    charlist[more].y -= 30


def level_up():
    global lev, en_delta_t, start_time_pop, item1, is_confuse, is_freeze, is_unbeatable, is_level_up
    lev += 1
    for j in range(2):
        delta_t_pop[j] -= vel_tube
        char_tube_word[j] = random.choice(wordlist)
        char_tube_word[j] = check_use(char_tube_word[j])
        if len(tube_upper_list[j]) >= 2:
            tube_upper_list[j] = [tube_upper_list[j][0], tube_upper_list[j][1]]
        else:
            while len(tube_upper_list[j]) < 2:
                stacktube(j)
        charlist[j].y = 210
    en_delta_t -= vel_plus
    item1 = item(800, 100)
    start_time_pop = [time.time(), time.time()]
    is_unbeatable = [time.time() - 3, time.time() - 3]
    is_freeze = [time.time() - 2, time.time() - 2]
    is_confuse = [time.time() - 3, time.time() - 3]
    is_level_up = time.time()


def poptube(more):
    global rep
    if len(tube_upper_list[more]) > 0:
        tube_upper_list[more].pop()
        charlist[more].y += 30
    else:
        if more == 0:
            rep = True
        else:
            level_up()


# 나와 상대 쪽에 튜브를 두 개씩 쌓는다.
for i in range(2):
    stacktube(0)
    stacktube(1)


# 아이템의 번호num=(item1.itemnum)와 0 또는 1의 more를 입력받는다.
# more가 0이면 내가 num에 해당하는 아이템을, 1이면 상대가 먹은 것.
def itemeffect(num, more):
    global item1
    global tube_under_list
    global tube_upper_list
    global charlist

    item1 = item(800, 100)
    item1.word = check_use(item1.word)
    if num == 1:
        charlist[more] = Charac(charlist[more].x, charlist[more].y)
    if num == 2:
        start_time_pop[more] += 3
    if num == 3:
        if time.time() - is_unbeatable[more] >= 3:
            for i in range(len(tube_upper_list[more])): poptube(more)
            start_time_pop[more] = time.time()
    if num == 4:
        is_unbeatable[more] = time.time()
    if num == 5:
        if more == 1 and time.time() - is_unbeatable[0] >= 3:
            is_confuse[0] = time.time()
        elif more == 0 and time.time() - is_unbeatable[1] >= 3:
            is_confuse[1] = time.time()
    if num == 6:
        for i in range(3): stacktube(more)
    if num == 7:
        if more == 1 and time.time() - is_unbeatable[0] >= 3:
            is_freeze[0] = time.time()
        elif more == 0 and time.time() - is_unbeatable[1] >= 3:
            is_freeze[1] = time.time()


while True:
    pygame.display.update()
    display.fill(White)
    printText("해상구조대 SOS", pos=(wid / 2 - 180, hei / 2 - 120), infon=4)
    printimage(Otherimage(wid / 2 - 100, hei / 2 - 10, 200, 200, "pyproimage/Play.png"))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if is_start and wid / 2 - 100 <= event.pos[0] < wid / 2 + 100 and hei / 2 - 10 <= event.pos[1] <= hei / 2 + 190:
                is_start = False
                time.sleep(0.5)
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if not is_start:
        break
    time.sleep(0.1)
    start_time_pop = [time.time(), time.time()]
    en_start_time = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = ([pygame.key.name(k) for k, v in enumerate(pressed) if v])
            for i in range(len(buttons)):
                if len(buttons) >= 2:
                    if pressed_button.count(buttons[i]) >= 1:
                        continue
                    pressed_button.append(buttons[i])
                    if buttons.count('left shift') >= 1 or buttons.count('right shift') >= 1 and len(buttons[i]) == 1:
                        buttons[i] = buttons[i].upper()
                else:
                    pressed_button = buttons
                if buttons[i] == 'backspace':
                    if len(texty) >= 1:
                        texty = texty[0:len(texty) - 1]
                    continue
                elif buttons[i] == 'return':
                    if time.time() - is_freeze[0] >= 2:
                        chk = False
                        if texty == item1.word:
                            itemvel += 0.05
                            score += 1
                            if time.time() - is_confuse[0] >=3 :
                                itemeffect(item1.itemnum, 0)
                            else:
                                itemeffect(item1.itemnum, 1)
                            chk = True
                        if not chk:
                            for j in range(4):
                                if texty == tube_under_list[j].word:
                                    if time.time() - is_confuse[0] >= 3:
                                        score += 1
                                        stacktube(0)
                                    else:
                                        stacktube(1)
                                    tube_under_list[j] = Tube(tube_under_list[j].x, tube_under_list[j].y)
                                    tube_under_list[j].word = check_use(tube_under_list[j].word)
                                    break
                            for j in range(2):
                                if len(tube_upper_list[j]):
                                    if time.time() - is_confuse[0] >= 3 and time.time() - is_unbeatable[j] >= 3:
                                        if texty == char_tube_word[j]:
                                            poptube(j)
                                            char_tube_word[j] = random.choice(wordlist)
                                            char_tube_word[j] = check_use(char_tube_word[j])
                                            break
                                    else:
                                        if texty == char_tube_word[j]:
                                            poptube(0)
                                            char_tube_word[j] = random.choice(wordlist)
                                            char_tube_word[j] = check_use(char_tube_word[j])
                                            break
                    texty = ""
                    continue
                elif buttons[0] == 'space':
                    texty += ' '
                    continue
                elif len(buttons[i]) > 1:
                    continue
                else:
                    texty = texty + buttons[i]
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rep and hei * 3 / 4 - 100 <= event.pos[1] <= hei * 3 / 4:
                if wid / 3 - 50 <= event.pos[0] <= wid / 3 + 50:  # 초기화
                    rep = False
                    texty = ""
                    pressed_button = []
                    score = 0
                    delta_t_pop = [7, 7]
                    start_time_pop = [time.time(), time.time()]
                    en_delta_t = 4
                    en_start_time = time.time()
                    com_move = 0
                    item1 = item(800, 100)
                    char_tube_word = [random.choice(wordlist), random.choice(wordlist)]
                    flag = False
                    tube_upper_list = [[], []]
                    pause_image = Otherimage(750, 0, 50, 50, "pyproimage/Pause.png")
                    itemvel = 2
                    sinx = [0, 0.8]
                    is_start = True
                    lev = 1
                    is_unbeatable = [time.time() - 3, time.time() - 3]
                    is_freeze = [time.time() - 2, time.time() - 2]
                    is_confuse = [time.time() - 3, time.time() - 3]
                    is_level_up = time.time() - 1
                    char1 = Charac(200, 270)
                    char2 = Charac(570, 270)
                    charlist = [char1, char2]
                    for i in range(2):
                        stacktube(0)
                        stacktube(1)
                    tube_under_list = []
                    for i in range(4):
                        temp = Tube(200 * i, 400)
                        temp.word = check_use(temp.word)
                        tube_under_list.append(temp)


                    continue
                elif wid * 2 / 3 - 50 <= event.pos[0]:
                    pygame.quit()
                    sys.exit()
            if event.pos[0] >= 750 and event.pos[1] <= 50:
                if flag:
                    flag = False
                else:
                    flag = True
                print("1")
        elif event.type == pygame.KEYUP:  # If user press any key.
            continue
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if flag:
        pygame.display.update()
        display.fill(White)
        printimage(pause_im1)
        printimage(play_image)
        for info in iteminfo: printimage(info)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(6):
                if iteminfo[i].x<=event.pos[0]<=iteminfo[i].x+100 and iteminfo[i].y<=event.pos[1]<=iteminfo[i].y+100:
                    boxflag=i
        if boxflag!=-1:
            printimage(informate[boxflag])
            printimage(boxes[boxflag])

        for i in range(2): start_time_pop[i] = 2 * time.time() - start_time_pop[i]
        en_start_time = 2 * time.time() - en_start_time
        continue
    if time.time() - en_start_time >= en_delta_t:
        com_move = random.randint(1, 3)
        en_start_time = time.time()
    if com_move == 1 and time.time() - is_freeze[1] >= 2:
        # 컴퓨터가 아이템을 먹는 부분
        if time.time() - is_confuse[1] >= 3:
            itemeffect(item1.itemnum, 1)
        else:
            itemeffect(item1.itemnum, 0)

    if com_move == 2 and time.time() - is_freeze[1] >= 2:
        # 컴퓨터가 튜브를 먹는 부분
        change = random.randrange(0, 4)
        tube_under_list[change] = Tube(tube_under_list[change].x, tube_under_list[change].y)
        tube_under_list[change].word = check_use(tube_under_list[change].word)
        if time.time() - is_confuse[1] >= 3:
            stacktube(1)
        else:
            stacktube(0)
    if com_move == 3 and time.time() - is_freeze[1] >= 2:
        if time.time() - is_confuse[1] >= 3 and time.time() - is_unbeatable[0] >= 3:
            poptube(0)
            char_tube_word[0] = random.choice(wordlist)
            char_tube_word[0] = check_use(char_tube_word[0])
        else:
            poptube(1)
            char_tube_word[1] = random.choice(wordlist)
            char_tube_word[1] = check_use(char_tube_word[1])
    com_move = 0
    if time.time() - start_time_pop[0] >= delta_t_pop[0]:
        poptube(0)
        start_time_pop[0] = time.time()

    if time.time() - start_time_pop[1] >= delta_t_pop[1]:
        poptube(1)
        start_time_pop[1] = time.time()
    for i in range(2):
        if len(tube_upper_list[i]) >= 7:
            if i == 0:
                level_up()
            else:
                rep = True
    if rep:
        pygame.display.update()
        display.fill(White)
        printText("Game end", pos=(wid / 2 - 75, hei / 2 - 215), infon=3)
        printText("Your score {}, replay?".format(score), pos=(wid / 2 - 185, hei / 3 * 2 - 150), infon=3)
        printimage(Otherimage(wid / 3 - 50, hei * 3 / 4 - 100, 100, 100, "pyproimage/yes.png"))
        printimage(Otherimage(wid / 3 * 2 - 50, hei * 3 / 4 - 100, 100, 100, "pyproimage/no.png"))
        continue

    pygame.display.update()
    display.fill(White)
    printimage(wallpaper)

    for i in range(2):
        printText('pop:' + (str)((int)(7 - (time.time() - start_time_pop[i]))), "Black",
                  (charlist[i].x + 27, charlist[i].y - 20), 2)
        if time.time() - is_unbeatable[i] < 3:
            printText("무적", "Black", (charlist[i].x + 35, charlist[i].y - 40), infon=5)
        if time.time() - is_freeze[i] < 2:
            printText("얼음", "Black", (charlist[i].x + 35, charlist[i].y - 40), infon=5)
        if time.time() - is_confuse[i] < 3:
            printText("혼란", "Black", (charlist[i].x + 15, charlist[i].y - 40), infon=5)
    for tubes in tube_under_list: printimage(tubes)
    for i in range(4):
        printText(tube_under_list[i].word, color="White", pos=(tube_under_list[i].x + 70, tube_under_list[i].y + 50))
    if time.time() - is_level_up < 1:
        printText('Level up!', 'BLACK', pos=(wid/2 - 80, 50), infon=3)
    shiver()

    # 나와 상대의 튜브 출력
    for tubes in tube_upper_list[0]:
        printimage(tubes)
    for tubes in tube_upper_list[1]:
        printimage(tubes)

    for chars in charlist: printimage(chars)
    for i in range(2):
        if len(tube_upper_list[i]) >= 1:
            printText(char_tube_word[i], 'White', (tube_upper_list[i][-1].x + 70, tube_upper_list[i][-1].y + 50))
    printimage(pause_image)

    printimage(item1)
    printText(item1.word, pos=(item1.x + 20, item1.y + 100))

    printText('Please enter the word')
    printText(texty, "black", (0, 532))
    printText('Score: ' + str(score), "black", (0, 0))
    printText('Level: ' + str(lev), "black", (0, 20))
    if item1.x > -100:
        item1.x -= itemvel
        if item1.x < -96:
            printimage(boom)
        if item1.x < -98:
            item1 = item(800, 100)
            item1.word = check_use(item1.word)

#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴
# https://pixlr.com/editor/ 에서 이미지 수정
