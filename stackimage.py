import pygame, sys
import random
import threading
import time

White = (255,255,255)
wid = 512
hei = 512

pygame.init()
display = pygame.display.set_mode((wid, hei))
display.fill(White)
pygame.display.set_caption("how_to_move")

class Charactor:
    def __init__(self,inputx,inputy):
        self.imagename1="C:/Users/user/Desktop/pyproimage/image"+(str)(random.randrange(0,10)+1)+".png"
        self.frog1 = pygame.image.load(self.imagename1) # 사진파일
        self.frog1 = pygame.transform.scale(self.frog1, (100,100))
        self.x1 = inputx
        self.y1 = inputy
        self.imagename2 = "C:/Users/user/Desktop/pyproimage/image" + (str)(random.randrange(0, 10) + 1) + ".png"
        self.frog2 = pygame.image.load(self.imagename2)  # 사진파일
        self.frog2 = pygame.transform.scale(self.frog2, (100, 100))
        self.x2 = inputx+50
        self.y2 = inputy+50

    def printloop(self):
        while True:
            '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    '''
            display.blit(self.frog1, (self.x1, self.y1))
            display.blit(self.frog2, (self.x2, self.y2))
            pygame.display.update()
            time.sleep(0.001)
            display.blit(self.frog1, (self.x1, self.y1))
            display.blit(self.frog2, (self.x2, self.y2))

    def print_char(self):
        thread_char = threading.Thread(target=self.printloop, args=())
        thread_char.start()

Ranger=Charactor(216,216)
Ranger.print_char()

Ranger=Charactor(400,400)
Ranger.print_char()

wallpaper="C:/Users/user/Desktop/pyproimage/image"+(str)(random.randrange(0,10)+1)+".png"
frog2 = pygame.image.load(wallpaper) # 사진파일
frog2 = pygame.transform.scale(frog2, (100,100))
x2 = 0
y2 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    display.blit(frog2, (x2, y2))


#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴