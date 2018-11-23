import pygame

def Main():
    pygame.init()
    font = pygame.font.Font("test.ttf", 40)
    text = font.render(u"안녕하세요", True, (255, 0, 0))

    screen = pygame.display.set_mode((320, 240))

    while True:
        for event in pygame.event.get():
            if pygame.KEYDOWN == event.type:
                if pygame.K_ESCAPE == event.key:
                    return
            if pygame.QUIT == event.type:
                return

        screen.fill((0, 0, 0))
        screen.blit(text, text.get_rect())
        pygame.display.flip()
