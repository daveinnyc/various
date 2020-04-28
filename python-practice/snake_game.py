# Modified version of code in https://www.youtube.com/watch?v=CD4qAhfFuLo
#   Improve variable naming clarity
#   Change camel case to underscores per PEP8
#   Suppress output line from pygame library
#   TODO: Add height, width, speed parameters 
#   TODO; Change magic numbers for colors to names


import os
import tkinter as tk
from tkinter import messagebox

# Suppress pygame output messages
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class cube(object):
    rows = 0
    w = 0
    
    def __init__(self, start, dirnx=0, diry=0, color=(255,0,0)):
        pass
        
    def move(self, dirnx, dirny):
        pass
        
    def draw(self, surface, eyes=False):
        pass
        
    
class snake(object):
    def __init__(self, color, pos):
        pass
    
    def move(self):
        pass
        
    def reset(self, pos):
        pass
        
    def add_cube(self):
        pass
        
    def draw(self, surface):
        pass
        


def draw_grid(width, rows, surface):
    block_size = width // rows
    x = 0
    y = 0
    
    for line in range(rows):
        x = x + block_size
        y = y + block_size
        
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))

    
def redraw_window(surface):
    global rows, width, height
    surface.fill((0, 0, 0))
    draw_grid(width, rows, surface)
    pygame.display.update()

    
def random_snack(rows, items):
    pass    

    
def message_box(subject, content):
    pass

    
def main():
    global rows, width, height    
    width = 500
    height = 500
    rows = 20
    window = pygame.display.set_mode((width, height))
    serpent = snake((255, 0, 0), (10, 10))
    delay = True
    
    clock = pygame.time.Clock()
    while delay:
        pygame.time.delay(50) # Lower values make game faster
        clock.tick(10)        # Lower values make game slower   
        redraw_window(window)
                
    
    
if __name__ == "__main__":
    rows = 0
    w = 0
    h = 0
        
    main()     