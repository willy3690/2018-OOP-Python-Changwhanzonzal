import pygame, sys, random, time

White = (255, 255, 255)
wid = 512
hei = 512
word_pool = ['최적부분구조']
Tube_list = []


class Player:
    def __init__(self, loc):
        self.loc = loc

    def Choose_tube(self):
        while True:
            input_word = input()
            try:
                temp = Tube_list.index(input_word)
            except IndexError:
                continue
            Tube_list.pop(temp)


class Tube:
    def __init__(self, identity):
        self.word = random.choice(word_pool)
        self.identity = identity

    pass


def Make_Tube(identity):
    New_Tube = Tube(identity)
    print(New_Tube)
