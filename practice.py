import pygame, sys

White = (255,255,255)
wid = 512
hei = 512


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


pygame.init()
display = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("how_to_move")
frog = pygame.image.load('C:/Users/willy/Desktop/sasa/python/images/frog_arrived.png') # 사진파일 
frog = pygame.transform.scale(frog, (50, 50))
y_change = 0
x_change = 0
x = wid * 0.05
y = hei * 0.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        moving()
        cannot_out()

    pygame.display.update()
    display.fill(White)
    display.blit(frog, (x, y))

#  https://blog.naver.com/rsj0908/221007425974  에서 가져옴
