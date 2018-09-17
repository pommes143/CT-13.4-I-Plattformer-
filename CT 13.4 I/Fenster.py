#! /usr/bin/python3
import pygame

class Fenster(object):
    width=0
    height=0
    """docstring for Fenster."""
    def __init__(self, screen_name, width, height, caption):
        self.height=height
        self.width=width
        super(Fenster, self).__init__()
        screen_name = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
