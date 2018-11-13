import pygame, sys

White = (255,255,255)
wid = 512
hei = 512

pygame.init()
display = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("tube")
frog = pygame.image.load('C:/Users/willy/Desktop/sasa/python/images/frog_arrived.png')
frog = pygame.transform.scale(frog, (50, 50))
x = wid * 0.5
y = hei * 0.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    display.fill(White)
    display.blit(frog, (x, y))
