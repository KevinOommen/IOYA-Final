import pygame ,sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.level=Level()

    def new(self):
        # start a new game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt=self.clock.tick()/1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.new()