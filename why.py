import pygame, sys
import random
import threading
import time

fp = open('pyprowords.txt', 'r')
wordlist = []
for line in fp:
    wordlist.append(line.strip())

def printimage(image):
    display.blit(image.frog,(image.x, image.y))


def printText(msg, color='BLACK', pos = (0, 512)):
    textSurface = font.render(msg, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    display.blit(textSurface,textRect)


White = (255,255,255)
wid = 800
hei = 512 + 50

pygame.init()
font = pygame.font.SysFont("consolas", 20)
display = pygame.display.set_mode((wid, hei))
display.fill(White)
pygame.display.set_caption("해상구조 SOS")
texty = ""
input_word = ""
pressed_button = list()
vel_plus = 0.05
delta_t = 5
start_time = time.time()


class item:
    def __init__(self, inputx, inputy, w, h):
        self.itemnum=random.randrange(0,10)+1
        self.imagename = "pyproimage/image"+(str)(self.itemnum)+".png"
        self.frog = pygame.image.load(self.imagename) # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w,h))
        self.x = inputx
        self.y = inputy
        self.word = random.choice(wordlist)


class Tube:
    def __init__(self, inputx, inputy, w=240, h=100):
        self.imagename="pyproimage/tubevector.png"
        self.frog = pygame.image.load(self.imagename) # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w, h))
        self.x = inputx
        self.y = inputy
        self.word = random.choice(wordlist)

class Charac:
    def __init__(self,inputx=200, inputy=200, w=100, h=100):
        self.charnum = random.randrange(1, 3) + 1
        self.imagename = "pyproimage/char" + (str)(self.charnum) + ".png"
        self.frog = pygame.image.load(self.imagename)  # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w, h))
        self.x = inputx
        self.y = inputy

class Otherimage:
    def __init__(self, inputx, inputy, w, h, imaname):
        self.imagename=imaname
        self.frog = pygame.image.load(self.imagename)  # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w, h))
        self.x = inputx
        self.y = inputy


wallpaper = Otherimage(0, 212, 800, 300, "pyproimage/wallpaper.png")
boom = Otherimage(-50, 100, 100, 100, "pyproimage/boom.png")
char1 = Charac()
onimage = Tube(130, 300)
onimage2 = Tube(130, 270)
item1 = item(800, 100, 100, 100)
pause_image = Otherimage(750, 0, 50, 50, "pyproimage/Pause.png")
pause_im1 = Otherimage(0, 0, wid, hei, "pyproimage/test_rule.png")
play_image = Otherimage(750, 0, 50, 50, "pyproimage/Play.png")

tube_list=[]
for i in range(4): tube_list.append(Tube(200*i,400))
tube_list.append(onimage)
tube_list.append(onimage2)
right=2
flag=False

score = float(0)
pause_image = Otherimage(750, 0, 50, 50, "pyproimage/Pause.png")
itemvel = 2

def stacktube():
    if len(tube_list)==4: new_player_tube = Tube(130, 300)
    else: new_player_tube = Tube(130, tube_list[len(tube_list) - 1].y - 30)
    tube_list.append(new_player_tube)
    char1.y = char1.y - 30

def itemeffect(num):
    global char1
    global item1
    item1 = item(800, 100, 100, 100)
    print(num)
    if num==7:
        for i in range(10): stacktube()
    if num==2: char1=Charac(char1.x,char1.y)


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = ([pygame.key.name(k) for k, v in enumerate(pressed) if v])
            for i in range(len(buttons)):
                if len(buttons) >= 2:
                    if pressed_button.count(buttons[i]) >= 1:
                        continue
                    elif buttons[-1] == 'left shift' or buttons[-1] == 'right shift':
                        for j in range(len(buttons)): buttons[j] = buttons[j].upper()
                        print(buttons)
                    else:
                        pressed_button.extend(buttons[i])
                else:
                    pressed_button = buttons
                if buttons[i] == 'backspace':
                    if len(texty) >= 1:
                        texty = texty[0:len(texty) - 1]
                    continue
                elif buttons[i] == 'return':
                    chk = False
                    if texty == item1.word:
                        itemvel += vel_plus
                        score += 1
                        itemeffect(item1.itemnum)
                        chk = True
                    if not chk:
                        for j in range(4):
                            if texty == tube_list[j].word:
                                score += 1
                                stacktube()
                                tube_list[j] = Tube(tube_list[j].x, tube_list[j].y)
                                break
                    texty = ""
                    continue
                elif buttons[0] == 'space' or buttons[0]=='SPACE':
                    texty += ' '
                    continue
                elif len(buttons[i]) > 1:
                    continue
                else:
                    texty = texty + buttons[i]
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
        start_time = 2 * time.time() - start_time
        continue
    if time.time() - start_time >= delta_t:
        if len(tube_list)>4:
            tube_list.pop()
        else:
            pygame.quit()
            sys.exit()
        char1.y = char1.y + 30
        start_time = time.time()
    if len(tube_list) >= 20:
        tube_list = [tube_list[0],tube_list[1],tube_list[2],tube_list[3],onimage, onimage2]
        delta_t -= 0.5
        char1.y = 200
        start_time = time.time()
    pygame.display.update()
    display.fill(White)
    printimage(wallpaper)

    for tubes in tube_list: printimage(tubes)
    for i in range(4):
        printText(tube_list[i].word, color= "White", pos=(tube_list[i].x + 70, tube_list[i].y + 50))

    printimage(pause_image)

    printimage(char1)
    printimage(item1)

    printText(item1.word, pos=(item1.x + 20, item1.y + 100))
    printText('Please enter the word')
    printText(texty, "black", (0, 532))
    printText('Score: ' + str(round(score, 1)), "black", (0, 0))
    if item1.x > -100:
        item1.x -= itemvel
        if item1.x < -96:
            printimage(boom)
            if item1.x < -98 and score > 0: score -= 0.1
        if item1.x < -98: item1 = item(800, 100, 100, 100)

#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴
# https://pixlr.com/editor/ 에서 이미지 수정
