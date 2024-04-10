import pygame

pygame.init()

pygame.display.set_caption("Rocket in Space!")

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

#define the player sprite. Player starts at (0,0) point

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("character.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100)) 


        