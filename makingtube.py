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
vel_plus = 0.01

class item:
    def __init__(self):
        self.imagename = "pyproimage/image"+(str)(random.randrange(0,10)+1)+".png"
        self.frog = pygame.image.load(self.imagename) # 사진파일
        self.frog = pygame.transform.scale(self.frog, (100,100))
        self.x = 800
        self.y = random.randrange(0,100)
        self.word = random.choice(wordlist)


class Tube:
    def __init__(self, inputx, inputy, w=240, h=100):
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
char1 = Otherimage(200, 200, 100, 100, "pyproimage/char2.png")
item1 = item()
tubelist=[]
for i in range(4): tubelist.append(Tube(200*i, 400))
tubelist.append(Tube(130, 250))
score = float(0)
itemvel = 1
right=1

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
                        item1 = item()
                        chk = True
                    if not chk:
                        for j in range(4):
                            if texty == tubelist[j].word:
                                score += 1
                                tubelist[j] = Tube(tubelist[j].x, tubelist[j].y)
                                char1.y-=40
                                tubelist.append(Tube(tubelist[4].x,tubelist[4].y-40*right))
                                right+=1
                                break
                    texty = ""
                    continue
                elif buttons[0] == 'space':
                    texty += ' '
                    continue
                elif len(buttons[i]) > 1: continue
                else: texty = texty + buttons[i]

        elif event.type == pygame.KEYUP: continue

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    display.fill(White)
    printimage(wallpaper)
    for tubes in tubelist:
        printimage(tubes)
    for i in range(4):
        printText(tubelist[i].word, color="White", pos=(tubelist[i].x + 70, tubelist[i].y + 50))

    printText(item1.word, pos=(item1.x + 20, item1.y + 100))
    printText('Please enter the word')
    printText(texty, "black", (0, 532))
    printText('Score: ' + str(round(score, 1)), "black", (0, 0))

    printimage(char1)
    move = [1.7, -1.7, 0]
    ymove = move[random.randrange(0, 3)]
    xmove = move[random.randrange(0, 3)]
    moverand=random.randrange(0,2)
    if moverand==0:
        if 210 > char1.x + xmove > 190: char1.x += xmove
    else:
        if 210 > char1.y + ymove > 190: char1.y += ymove

    printimage(item1)
    if item1.x > -100:
        item1.x -= itemvel
        if item1.x < -96:
            printimage(boom)
            if item1.x < -98 and score > 0: score -= 0.1
        if item1.x < -98: item1 = item()

#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴
# https://pixlr.com/editor/ 에서 이미지 수정