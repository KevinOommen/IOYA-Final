import pygame
from settings import *
from random import randint,choice
from timer1 import Timer


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
    def __init__(self,pos,surf,groups,name,all_sprites):
        super().__init__(pos,surf,groups)
        self.hitbox=self.rect.copy().inflate((-self.rect.width * 0.2,-self.rect.height * 0.75))
        self.all_sprites = all_sprites

       # tree attributes
        self.health=5
        self.alive=True
        stump_path=f'../graphics/stumps/{"small" if name == "Small" else "large"}.png'
        self.stump_surf=pygame.image.load(stump_path).convert_alpha()
        self.invul_timer=Timer(200)
         
        self.apple_surf=pygame.image.load('../graphics/fruit/apple.png')
        self.apple_pos=APPLE_POS[name]
        self.apple_sprites=pygame.sprite.Group()
        self.create_fruit()


    def damage(self):

        self.health-=1
        #remove apple
        if len(self.apple_sprites()) > 0:
            random_apple=choice(self.apple_sprites.sprites())
            random_apple.kill()

    def create_fruit(self):
        all_sprites_group = self.all_sprites
        for pos in self.apple_pos:
           if randint(0,10)<2: 
                x=pos[0]+self.rect.left
                y=pos[1]+self.rect.top
                Generic(
                    pos=(x,y),
                    surf=self.apple_surf,
                    groups=[self.apple_sprites,all_sprites_group],
                    z=LAYERS['fruit']
                    )
