from pygame.math import Vector2 
import pygame ,sys

#screen settings
WIDTH, HEIGHT = 1200, 600
TITLE = "IOYA:THE STRUGGLE"
FPS = 60
TILESIZE = 64

# overlay positions 
OVERLAY_POSITIONS = {
	'tool' : (40, HEIGHT - 15), 
	'seed': (70, HEIGHT - 5)
}


LAYERS = {
	'water': 0,
	'ground': 1,
	'soil': 2,
	'soil water': 3,
	'rain floor': 4,
	'house bottom': 5,
	'ground plant': 6,
	'main': 7,
	'house top': 8,
	'fruit': 9,
	'rain drops': 10
}