#! /usr/bin/python3
import pygame
from Fenster import *
class Steuerung():
    running = True

    def start():
        pygame.init()
        DieSteuerung = Steuerung()

    def __init__(self):
        Spiel_Fenster = Fenster("spiel_fenster", 800, 700, "Cooles krasses Spiel")

        self.schleife()

    def schleife(self):
        pygame.time.delay(100)
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                pass
            if keys[pygame.K_a]:
                pass
            if keys[pygame.K_s]:
                pass
            if keys[pygame.K_d]:
                pass

        pygame.quit()
