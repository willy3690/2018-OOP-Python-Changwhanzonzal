import pygame, sys
import random
import threading

White = (255,255,255)
wid = 512
hei = 512

'''
def cannot_out():
    global x,y
    if x < 0:
        x = 0
    if x > 462:
        x = 462
    elif y < 0:
        y = 0
    elif y > 462:
        y = 462


def moving():
    global y_change, x_change, x, y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            y_change = y_change + 30
        if event.key == pygame.K_UP:
            y_change = y_change - 30
        if event.key == pygame.K_LEFT:
            x_change = x_change - 30
        if event.key == pygame.K_RIGHT:
            x_change = x_change + 30
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                y_change = 0
        x += x_change
        y += y_change
'''

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