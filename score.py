import pygame, sys
import random
import threading
import time
import random
fp = open('pyprowords.txt', 'r')
wordlist=[]
for line in fp:
    wordlist.append(line.strip())

def printimage(image):
    display.blit(image.frog,(image.x,image.y))


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

class item:
    def __init__(self,inputx,inputy,wid,hei):
        self.imagename="C:/Users/user/Desktop/pyproimage/image"+(str)(random.randrange(0,10)+1)+".png"
        self.frog = pygame.image.load(self.imagename) # 사진파일
        self.frog = pygame.transform.scale(self.frog, (wid,hei))
        self.x = inputx
        self.y = inputy


class Tube:
    def __init__(self,inputx,inputy,wid,hei):
        self.imagename="pyproimage/tubevector.png"
        self.frog = pygame.image.load(self.imagename) # 사진파일
        self.frog = pygame.transform.scale(self.frog, (wid,hei))
        self.x = inputx
        self.y = inputy


class Otherimage:
    def __init__(self,inputx,inputy,wid,hei,imaname):
        self.imagename=imaname
        self.frog = pygame.image.load(self.imagename)  # 사진파일
        self.frog = pygame.transform.scale(self.frog, (wid, hei))
        self.x = inputx
        self.y = inputy


wallpaper=Otherimage(0,212,800,300,"pyproimage/wallpaper.png")
boom=Otherimage(-50,100,100,100,"pyproimage/boom.png")
char1=Otherimage(80,350,100,100,"pyproimage/char2.png")
onimage=Tube(10,400,240,100)
item1=item(800,100,100,100)

score=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = ([pygame.key.name(k) for k, v in enumerate(pressed) if v])
            for i in range(len(buttons)):
                if len(buttons) >= 2:
                    if pressed_button.count(buttons[i]) >= 1:
                        continue
                    elif (buttons[1]=='left shift'):
                        buttons[0]=buttons[0].upper()
                    else:
                        pressed_button.extend(buttons[i])
                else:
                    pressed_button = buttons
                if buttons[i] == 'backspace':
                    if len(texty) >= 1:
                        texty = texty[0:len(texty) - 1]
                    continue
                elif buttons[i] == 'return':
                    if (texty == wordlist[0]):
                        score += 1
                        item1 = item(800, 100, 100, 100)
                    input_word = texty
                    texty = ""
                    random.shuffle(wordlist)
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
    pygame.display.update()
    display.fill(White)
    printimage(wallpaper)
    printimage(onimage)
    printimage(char1)
    printimage(item1)

    printText(wordlist[0],"black",(300,512))
    printText('Please enter the word')
    printText(texty, "black", (0, 532))
    printText('Score: '+str(score),"black",(0,0))

    move=[2, -2, 0]
    ymove = move[random.randrange(0, 3)]
    xmove = move[random.randrange(0, 3)]
    if char1.x+xmove<90 and char1.x+xmove>70: char1.x+=xmove
    if char1.y + ymove < 360 and char1.y + ymove > 340: char1.y+=ymove
    if(item1.x>-100):
        item1.x-=2
        if(item1.x<-96):
            printimage(boom)
        if(item1.x<-98): item1 = item(800, 100, 100, 100)

#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴
# https://pixlr.com/editor/ 에서 이미지 수정