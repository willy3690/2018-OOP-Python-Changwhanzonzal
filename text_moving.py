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
        self.imagename = "pyproimage/image"+(str)(random.randrange(0,10)+1)+".png"
        self.frog = pygame.image.load(self.imagename) # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w,h))
        self.x = inputx
        self.y = inputy
        self.word = random.choice(wordlist)


class Tube:
    def __init__(self, inputx, inputy, w, h):
        self.imagename="pyproimage/tubevector.png"
        self.frog = pygame.image.load(self.imagename) # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w, h))
        self.x = inputx
        self.y = inputy
        self.word = random.choice(wordlist)


class Otherimage:
    def __init__(self, inputx, inputy, w, h, imaname):
        self.imagename=imaname
        self.frog = pygame.image.load(self.imagename)  # 사진파일
        self.frog = pygame.transform.scale(self.frog, (w, h))
        self.x = inputx
        self.y = inputy


wallpaper = Otherimage(0, 212, 800, 300, "pyproimage/wallpaper.png")
boom = Otherimage(-50, 100, 100, 100, "pyproimage/boom.png")
char1 = Otherimage(200, 250, 100, 100, "pyproimage/char2.png")
onimage = Tube(130, 300, 240, 100)
item1 = item(800, 100, 100, 100)
tube1 = Tube(0, 400, 240, 100)
tube2 = Tube(200, 400, 240, 100)
tube3 = Tube(400, 400, 240, 100)
tube4 = Tube(600, 400, 240, 100)
score = float(0)
itemvel = 1
tube_word = [tube1.word, tube2.word, tube3.word, tube4.word]
tube_list = [onimage]


def del_tube(temp1, temp2):
    t = Tube(temp1, 400, 240, 100)
    tube_word[temp2] = t.word
    return t


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = ([pygame.key.name(k) for k, v in enumerate(pressed) if v])
            for i in range(len(buttons)):
                if len(buttons) >= 2:
                    if pressed_button.count(buttons[i]) >= 1:
                        continue
                    elif buttons[1] == 'left shift':
                        buttons[0] = buttons[0].upper()
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
                        item1 = item(800, 100, 100, 100)
                        chk = True
                    if not chk:
                        for j in range(4):
                            if texty == tube_word[j]:
                                score += 1
                                new_player_tube = Tube(130, tube_list[-1].y - 50, 250, 100)
                                char1.y = char1.y - 50
                                tube_list.append(new_player_tube)
                                if j == 0:
                                    tube1 = del_tube(0, 0)
                                    break
                                elif j == 1:
                                    tube2 = del_tube(200, 1)
                                    break
                                elif j == 2:
                                    tube3 = del_tube(400, 2)
                                    break
                                else:
                                    tube4 = del_tube(600, 3)
                    texty = ""
                    continue
                elif buttons[0] == 'space':
                    texty += ' '
                    continue
                elif len(buttons[i]) > 1:
                    continue
                else:
                    texty = texty + buttons[i]
        elif event.type == pygame.KEYUP:  # If user press any key.
            continue
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if time.time() - start_time >= delta_t:
        try:
            tube_list.pop()
        except IndexError:
            pygame.quit()
            sys.exit()
        char1.y = char1.y + 50
        start_time = time.time()
    pygame.display.update()
    display.fill(White)
    printimage(wallpaper)
    for i in tube_list:
        printimage(i)
    printimage(char1)
    printimage(item1)
    printimage(tube1), printimage(tube2), printimage(tube3), printimage(tube4)
    printText(tube1.word, color= "White", pos=(tube1.x + 70, tube1.y + 50))
    printText(tube2.word, color= "White", pos=(tube2.x + 70, tube2.y + 50))
    printText(tube3.word, color= "White", pos=(tube3.x + 70, tube3.y + 50))
    printText(tube4.word, color= "White", pos=(tube4.x + 70, tube4.y + 50))
    printText(item1.word, pos=(item1.x + 20, item1.y + 100))
    printText('Please enter the word')
    printText(texty, "black", (0, 532))
    printText('Score: ' + str(round(score, 1)), "black", (0, 0))

    move = [2, -2, 0]
    ymove = move[random.randrange(0, 3)]
    xmove = move[random.randrange(0, 3)]
    if 90 > char1.x + xmove > 70: char1.x += xmove
    if 360 > char1.y + ymove > 340: char1.y += ymove
    if item1.x > -100:
        item1.x -= itemvel
        if item1.x < -96:
            printimage(boom)
            if item1.x < -98 and score > 0: score -= 0.1
        if item1.x < -98: item1 = item(800, 100, 100, 100)

#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴
# https://pixlr.com/editor/ 에서 이미지 수정