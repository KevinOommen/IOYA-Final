import pygame
import check
from settings import *
from support import import_folder
from timer1 import Timer
import tkinter as tk
from tkinter import messagebox
import sprites

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites, tree_sprites):
        super().__init__(group)

        self.import_assets()

        self.status = 'down'
        self.frame_index = 0

        # general setup
        self.image = self.animation[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS['main']

        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        # collision
        self.hitbox = self.rect.copy().inflate((-126, -70))
        self.collision_sprites = collision_sprites

        # timers
        self.timers = {
            'tool use': Timer(500, self.use_tool),
            'tool switch': Timer(200)
        }

        # tools
        self.tools = ['hoe', 'axe', 'water']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]

        # interaction
        self.tree_sprites = tree_sprites

    def use_tool(self):
        if self.selected_tool == 'hoe':
            pass
        if self.selected_tool == 'axe':
            for tree in self.tree_sprites.sprites():
                if tree.rect.collidepoint(self.target_pos):
                    tree.damage()

        if self.selected_tool == 'water':
            pass

    def get_target_pos(self):
        self.target_pos = self.rect.center + PLAYER_TOOL_OFFSET[self.status.split('_')[0]]

    def import_assets(self):
        self.animation = {
            'up': [],
            'down': [],
            'left': [],
            'right': [],
            'right_idle': [],
            'left_idle': [],
            'up_idle': [],
            'down_idle': [],
            'right_axe': [],
            'left_axe': [],
            'up_axe': [],
            'down_axe': [],
            'right_hoe': [],
            'left_hoe': [],
            'up_hoe': [],
            'down_hoe': [],
            'right_water': [],
            'left_water': [],
            'up_water': [],
            'down_water': [],
        }
        for animation in self.animation.keys():
            full_path = '../graphics/character/' + animation
            self.animation[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 4 * dt

        if self.frame_index >= len(self.animation[self.status]):
            self.frame_index = 0

        self.image = self.animation[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.timers['tool use'].active:
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0

            # tool use
            if keys[pygame.K_SPACE]:
                self.timers['tool use'].activate()
                self.direction = pygame.math.Vector2(0, 0)
                self.frame_index = 0

            # tool selection
            if keys[pygame.K_q] and not self.timers['tool switch'].active:
                self.timers['tool switch'].activate()
                self.tool_index += 1
                self.selected_tool = self.tools[self.tool_index % len(self.tools)]
    def ok_button_pressed_function(self,npc_id):
    # Define your function to be called when the OK button is pressed
        print("OK button pressed!")
        
        c=check.check(npc_id, 1)
        if c==1:
            print("Correct submission")
            self.show_popup2("Correct submission")
        else:
            print("Wrong submission")
            self.show_popup2("Wrong submission")
    
    def show_popup(self,message,npc_id):
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window

        # Show the pop-up
        # messagebox.showinfo("Popup", message)
        result = messagebox.askokcancel("Popup", message)

        # Destroy the Tkinter window to prevent it from lingering in the background
        root.destroy()

        if result:
            self.ok_button_pressed_function(npc_id)

    def show_popup2(self,message):
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window

        # Show the pop-up
        # messagebox.showinfo("Popup", message)
        result = messagebox.askokcancel("Popup", message)

        # Destroy the Tkinter window to prevent it from lingering in the background
        root.destroy()


    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if self.hitbox.colliderect(sprite.hitbox):
                    if isinstance(sprite,sprites.Tree):  
                        if sprite.name=='Small':
                            print(sprite.name)
                            # Assuming your tree class is named 'Tree'
                            npc_id=npc_id. get_npc_id_by_name('chitra')
                            self.show_popup('You hit a chitra',npc_id)
                            

                        elif sprite.name=='Medium':
                            npc_id=npc_id. get_npc_id_by_name('veena')# Assuming your tree class is named 'Tree'
                            self.show_popup('You hit a veena',npc_id)
                        elif sprite.name=='Large':# Assuming your tree class is named 'Tree'
                            npc_id=npc_id. get_npc_id_by_name('anisha',npc_id)
                            self.show_popup('You hit a anisha',npc_id)
                    
                    if direction == 'horizontal':
                        if self.direction.x > 0:
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0:
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                    if direction == 'vertical':
                        if self.direction.y > 0:
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

    def move(self, dt):
        # normalize vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

            # horizontal movement
            self.pos.x += self.direction.x * self.speed * dt
            self.hitbox.centerx = round(self.pos.x)
            self.rect.centerx = self.hitbox.centerx
            self.collision('horizontal')

            # vertical movement
            self.pos.y += self.direction.y * self.speed * dt
            self.hitbox.centery = round(self.pos.y)
            self.rect.centery = self.hitbox.centery
            self.collision('vertical')

    def get_status(self):
        # idle
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
        # tool use
        if self.timers['tool use'].active:
            print('tool use')
            self.status = self.status.split('_')[0] + '_' + self.selected_tool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.get_target_pos()

        self.move(dt)
        self.animate(dt)
