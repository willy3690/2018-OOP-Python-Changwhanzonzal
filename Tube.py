import pygame, sys, random, time, threading

White = (255, 255, 255)
wid = 512
hei = 512
word_pool = ['최적부분구조']
Tube_list = []
pygame.init()
display = pygame.display.set_mode((wid, hei))
pygame.display.set_caption("how_to_move")
Tube_image = pygame.image.load('C:/Users/user/Pictures/testimage1.png')
Tube_image = pygame.transform.scale(Tube_image, (50, 50))
x = 10
y = 10
loc_num_x = (100, 200, 300, 400)
loc_num_y = (400, 400, 400, 400)


def Show_Tube(a, b):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        display.fill(White)
        display.blit(Tube_image, (a, b))
        time.sleep(1000)


class Player:
    def __init__(self, loc, input_word):
        self.loc = loc
        self.input_word = input_word

    def Choose_tube(self):
        while True:
            try:
                temp = Tube_list.index(self.input_word)
            except IndexError:
                continue
            Tube_list.pop(temp)


class Tube:
    def __init__(self, identity):
        self.word = random.choice(word_pool)
        self.identity = identity

    def print_Tube(self):
        if self.identity == 1 or self.identity == 2 or self.identity == 3 or self.identity == 4:
            temp_thread = threading.Thread(target=Show_Tube, args=(loc_num_x[self.identity-1], loc_num_y[self.identity-1]))
            temp_thread.start()



tube_1 = Tube(1)
tube_2 = Tube(2)
tube_3 = Tube(3)
tube_4 = Tube(4)
tube_1.print_Tube()
tube_2.print_Tube()
tube_3.print_Tube()
tube_4.print_Tube()
