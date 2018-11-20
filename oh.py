import pygame, sys
import random
#it is not important to change
import threading

White = (255,255,255)
wid = 512
hei = 512

pygame.init()
display = pygame.display.set_mode((wid, hei))
display.fill(White)
pygame.display.set_caption("how_to_move")


imagename1="C:/Users/user/Pictures/testimage"+(str)(random.randrange(0,3))+".png"
frog1 = pygame.image.load(imagename1) # 사진파일
frog1 = pygame.transform.scale(frog1, (100,100))
x1 = wid/2-50
y1 = hei/2-50

def printfrog1():
    global frog1,x1,y1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        display.blit(frog1, (x1, y1))

thread_recv = threading.Thread(target=printfrog1, args=())
thread_recv.start()


imagename2="C:/Users/user/Pictures/testimage"+(str)(random.randrange(0,3))+".png"
frog2 = pygame.image.load(imagename2) # 사진파일
frog2 = pygame.transform.scale(frog2, (100,100))
x2 = 50
y2 = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    display.blit(frog2, (x2, y2))


#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴