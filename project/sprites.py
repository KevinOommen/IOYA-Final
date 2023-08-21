import pygame
from settings import *


class Generic(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups,z=LAYERS['main']):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_rect(topleft=pos)
        self.z=z
        self.hitbox=self.rect.copy().inflate((-self.rect.width * 0.2,-self.rect.height * 0.75))


class Wildflower(Generic):
    def __init__(self,pos,surf,groups):
        super().__init__(pos,surf,groups)
        self.hitbox=self.rect.copy().inflate((-20,-self.rect.height * 0.9))



class Tree(Generic):
    def __init__(self,pos,surf,groups,name):
        super().__init__(pos,surf,groups)
        self.hitbox=self.rect.copy().inflate((-self.rect.width * 0.2,-self.rect.height * 0.75))
