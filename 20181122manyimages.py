import pygame, sys
import random
import threading
import time

White = (255,255,255)
wid = 800
hei = 512

pygame.init()
display = pygame.display.set_mode((wid, hei))
display.fill(White)
pygame.display.set_caption("how_to_move")

class Charactor:
    def __init__(self,inputx,inputy,wid,hei):
        self.imagename="C:/Users/user/Desktop/pyproimage/image"+(str)(random.randrange(0,10)+1)+".png"
        self.frog = pygame.image.load(self.imagename) # 사진파일
        self.frog = pygame.transform.scale(self.frog, (wid,hei))
        self.x = inputx
        self.y = inputy

class Tube:
    def __init__(self,inputx,inputy,wid,hei):
        self.imagename="C:/Users/user/Desktop/pyproimage/tubevector.png"
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

wallpaper=Otherimage(0,212,800,300,"C:/Users/user/Desktop/pyproimage/wallpaper.png")

char1=Otherimage(80,350,100,100,"C:/Users/user/Desktop/pyproimage/char2.png")

onimage=Tube(10,400,240,100)

def displayblit(image):
    display.blit(image.frog,(image.x,image.y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    time.sleep(0.1)
    displayblit(wallpaper)
    displayblit(onimage)
    displayblit(char1)
    '''
    display.blit(wallpaper.frog, (wallpaper.x, wallpaper.y))
    display.blit(onimage.frog, (onimage.x, onimage.y))
    display.blit(char1.frog, (char1.x, char1.y))
    '''

#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴
# https://pixlr.com/editor/ 에서 이미지 수정