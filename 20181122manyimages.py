import pygame, sys
import random
import threading
import time

def printimage(image):
    display.blit(image.frog,(image.x,image.y))

White = (255,255,255)
wid = 800
hei = 512

pygame.init()
display = pygame.display.set_mode((wid, hei))
display.fill(White)
pygame.display.set_caption("해상구조 SOS")

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
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    time.sleep(0.0001)
    display.fill(White)
    printimage(wallpaper)
    printimage(onimage)
    printimage(char1)
    move=[2, -2, 0]
    ymove = move[random.randrange(0, 3)]
    xmove = move[random.randrange(0, 3)]
    if char1.x+xmove<90 and char1.x+xmove>70: char1.x+=xmove
    if char1.y + ymove < 360 and char1.y + ymove > 340: char1.y+=ymove

#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴
# https://pixlr.com/editor/ 에서 이미지 수정