import pygame
from settings import *
from random import randint, choice
from timer1 import Timer
import tkinter as tk
from tkinter import messagebox
SCREEN_WIDTH ,SCREEN_HEIGHT= 1280, 720
class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z=LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate((-self.rect.width * 0.2, -self.rect.height * 0.75))


class Wildflower(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy().inflate((-20, -self.rect.height * 0.9))


class Tree(Generic):
    def __init__(self, pos, surf, groups, name, all_sprites):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy().inflate((-self.rect.width * 0.2, -self.rect.height * 0.75))
        self.all_sprites = all_sprites
        self.name = name  # Added attribute for the name

        # tree attributes
        self.health = 5
        self.alive = True
        # stump_path = '../graphics/objects/tree_small.png'
        # self.stump_surf = pygame.image.load(stump_path).convert_alpha()
        self.invul_timer = Timer(200)

    def damage(self):
        self.health -= 1

        # Show popup based on the tree's name
        self.show_popup()

    def show_popup(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window

        # Show a popup with a message based on the tree's name
        # if self.name == "Small":
        #     messagebox.showinfo("Tree Popup", "You damaged a small tree!")
        # elif self.name == "Medium":
        #     messagebox.showinfo("Tree Popup", "You damaged a medium tree!")
        # elif self.name == "Large":
        #     messagebox.showinfo("Tree Popup", "You damaged a large tree!")

        # Destroy the Tkinter window to prevent it from lingering in the background
        root.destroy()

    # def create_fruit(self):
    #     all_sprites_group = self.all_sprites
    #     for pos in APPLE_POS[self.name]:
    #         if randint(0, 10) < 2:
    #             x = pos[0] + self.rect.left
    #             y = pos[1] + self.rect.top
    #             Generic(
    #                 pos=(x, y),
    #                 surf=self.apple_surf,
    #                 groups=[self.apple_sprites, all_sprites_group],
    #                 z=LAYERS['fruit']
    #             )

# Game setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Assume you have a list of tree names
tree_names = ["veena", "chitra", "anisha"]

# Create a sprite group to manage all sprites
all_sprites = pygame.sprite.LayeredUpdates()

# Create Tree instances for each tree name
for tree_name in tree_names:
    tree_pos = (randint(0, SCREEN_WIDTH - 1), randint(0, SCREEN_HEIGHT - 1))
    print(tree_name)  # Random position
    tree_path = f'../graphics/objects/{tree_name.lower()}.png'  # Static path for all trees
    
    tree_surf = pygame.image.load(tree_path).convert_alpha()
    tree = Tree(tree_pos, tree_surf, all_sprites, tree_name, all_sprites)
    # tree.create_fruit()  # Optionally create fruit for each tree

# Main game loop
# running = True
# while running:
#     dt = clock.tick(FPS) / 1000  # Convert milliseconds to seconds

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Update all sprites
#     all_sprites.update(dt)

#     # Draw all sprites
#     # screen.fill(BG_COLOR)
#     all_sprites.draw(screen)
#     pygame.display.flip()

# pygame.quit()
