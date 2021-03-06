#sdfafsd
import pygame, sys
import random
import threading
import time


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
font = pygame.font.SysFont("나눔 손글씨 붓", 30)
display = pygame.display.set_mode((wid, hei))
display.fill(White)
pygame.display.set_caption("해상구조 SOS")
texty = ""
flag = False
input_word = ""


class Charactor:
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
char1=Otherimage(80,350,100,100,"pyproimage/char2.png")
onimage=Tube(10,400,240,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            buttons = ([pygame.key.name(k) for k, v in enumerate(pressed) if v])
            print(buttons)
            if len(buttons)==0:
                texty+='한영키'
                continue
            elif buttons[0] == 'backspace':
                if len(texty) >= 1:
                    texty = texty[0:len(texty) - 1]
                continue
            elif buttons[0] == 'return':
                input_word = texty
                texty = ""
                continue
            elif buttons[0] == 'left shift' or buttons[0]=='right shift':
                texty+='shift!'
                print(buttons)
                continue
            elif buttons[0] == 'space':
                texty+=' '
                continue
            elif len(buttons[0]) > 1:
                continue
            else:
                texty = texty + buttons[0]
            flag = True
        elif event.type == pygame.KEYUP:  # If user press any key.
            flag = False
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    #time.sleep(0.1)
    display.fill(White)
    printimage(wallpaper)
    printimage(onimage)
    printimage(char1)

    printText('Please enter the word')
    printText('안녕',"black",(400,512))
    printText(texty, "black", (0, 532))

    move=[0.2, -0.2, 0]
    ymove = move[random.randrange(0, 3)]
    xmove = move[random.randrange(0, 3)]
    if char1.x+xmove<90 and char1.x+xmove>70: char1.x+=xmove
    if char1.y + ymove < 360 and char1.y + ymove > 340: char1.y+=ymove

#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴
# https://pixlr.com/editor/ 에서 이미지 수정