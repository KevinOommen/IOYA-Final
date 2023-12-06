from tkinter import messagebox
import tkinter
import pygame ,sys
import picktask
import task_desc
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.level=Level()
    def show_popup(self,msg):
        root = tkinter.Tk()
        root.withdraw()  # Hide the main Tkinter window

        # Show a popup with a message based on the tree's name
    
        messagebox.showinfo("Your Task", msg)
      

        # Destroy the Tkinter window to prevent it from lingering in the background
        root.destroy()
    def new(self):
        # start a new game
        t=picktask.PickTask(1)
        print(t)
        k=task_desc.Task_Desc(t)
        self.show_popup(f"Your Task is to {k}")


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