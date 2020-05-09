#   Refactor game code for clarity, style, improved quality
#   Original code from https://www.youtube.com/watch?v=CD4qAhfFuLo
#
#   ADDED: if __name__ section for better modularity
#   ADDED: Add reasonable title to pygame window
#
#   FIXED: Improve variable naming clarity
#   FIXED: Change camel case to underscores per PEP8
#   FIXED: Change class names to CapWords convention
#   FIXED: Suppress output line from pygame library
#   FIXED: make object initialization variable in Cube class
#   FIXED: Change magic numbers for colors to names
#   FIXED: Get rid of global variables
#   FIXED: Cube dimensions should not be hard coded
#   
#   TODO: Add height, width, speed parameters 
#   TODO: Random starting point
#   TODO: Random starting point on reset
#   TODO: Clean up eye drawing code
#   TODO: rows, columns may not always be equal numbers
#   TODO: Check lambdas that look for collisions
#   TODO: display current score
#   TODO: improve score display on collision
#
#   ON HOLD 
#   TODO: Add 'no' to play again dialog --> pygame doesn't appear to have dialog boxes


import snake_constants as const
import os
import random
import tkinter as tk
from tkinter import messagebox

# Suppress pygame output messages
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Cube():
    rows = 0
    width = 0
    height = 0
    
    def __init__(self, start, direction_x=0, direction_y=0, color=(255,0,0)):
        self.pos = start
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.color = color
        
    def move(self, direction_x, direction_y):
        self.direction_x = direction_x
        self.direction_y = direction_y
        # Position counts in units of Cubes, not in units of pixels 
        self.pos = (self.pos[0] + self.direction_x, self.pos[1] + self.direction_y)
        
    def draw(self, surface, eyes=False):
        dis = self.width // self.rows
        
        x = self.pos[0]
        y = self.pos[1]
        # Offsets are to preserve visibility of the grid
        pygame.draw.rect(surface, self.color, (x * dis + 1, y * dis + 1, dis - 2, dis - 2))
        
        if eyes: 
            center = dis // 2     # Cube center
            radius = 3            # Eye radius
            circle_middle = (x * dis + center - radius, y * dis + 8)
            circle_middle2 = (x * dis + dis - radius * 2, y * dis + 8)
            pygame.draw.circle(surface, const.BLACK, circle_middle, radius)
            pygame.draw.circle(surface, const.BLACK, circle_middle2, radius)
            
        
        
    
class Snake():
    body = []
    turns = {}
    
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.direction_x = 0    # Possible values (-1, 0, 1)
        self.direction_y = 1    # Possible values (-1, 0, 1)
        
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.direction_x = -1
                    self.direction_y = 0 
                    # ??? Why copying list for head?
                    self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
                    
                elif keys[pygame.K_RIGHT]:
                    self.direction_x = 1
                    self.direction_y = 0 
                    # ??? Why copying list for head?
                    self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                elif keys[pygame.K_UP]:
                    self.direction_x = 0
                    self.direction_y = -1 
                    # ??? Why copying list for head?
                    self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                elif keys[pygame.K_DOWN]:
                    self.direction_x = 0
                    self.direction_y = 1 
                    # ??? Why copying list for head?
                    self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
                    
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == (len(self.body) - 1):
                    self.turns.pop(p)
            else:
                if c.direction_x == -1 and c.pos[0] <= 0: 
                    c.pos = (c.rows - 1, c.pos[1])            
                elif c.direction_x == 1 and c.pos[0] >= c.rows - 1: 
                    c.pos = (0, c.pos[1])            
                elif c.direction_y == 1 and c.pos[1] >= c.rows - 1: 
                    c.pos = (c.pos[0], 0)            
                elif c.direction_y == -1 and c.pos[1] <= 0: 
                    c.pos = (c.pos[0], c.rows - 1)            
                else:
                    c.move(c.direction_x, c.direction_y)            
        
        
    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.direction_x = 0
        self.direction_y = 1
        
        
    def add_Cube(self):
        tail = self.body[-1]
        dx, dy = tail.direction_x, tail.direction_y
        
        # Check direction tail is moving and add new Cube accordingly
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))
        
        self.body[-1].direction_x = dx
        self.body[-1].direction_y = dy
        
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                # The first Cube has eyes
                c.draw(surface, True)
            else:
                c.draw(surface)
        


def draw_grid(width, rows, surface):
    block_size = width // rows
    x = 0
    y = 0
    
    for line in range(rows):
        x = x + block_size
        y = y + block_size
        
        pygame.draw.line(surface, const.WHITE, (x, 0), (x, width))
        pygame.draw.line(surface, const.WHITE, (0, y), (width, y))

    
def redraw_window(surface, rows, width, snake, snack):
    surface.fill((const.BLACK))
    snake.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()

    
def random_snack(rows, snake):
    # TODO: rows, columns may not always be equal numbers
    positions = snake.body
    
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
            
    return (x,y)        

    
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    # Click to dismiss, no obvious way to convert message box to dialog box
    messagebox.showinfo(subject, content)
    try: 
        root.destroy()
    except:
        pass

    
def main(set_rows, set_width, set_height):
    width = set_width
    height = set_height
    rows = set_rows
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Feed the snake!')
    serpent = Snake(const.RED, (10, 10))
    snack = Cube(random_snack(rows, serpent), color=const.GREEN)
    delay = True
    
    clock = pygame.time.Clock()
    while delay:
        pygame.time.delay(65) # Lower values make game faster
        clock.tick(8)         # Lower values make game slower   
        serpent.move()
        if serpent.body[0].pos == snack.pos:
            serpent.add_Cube()
            snack = Cube(random_snack(rows, serpent), color=const.GREEN)
            
        for x in range(len(serpent.body)):
            if serpent.body[x].pos in list(map(lambda z:z.pos, serpent.body[x+1:])):
                print(f"Score: {len(serpent.body)}")
                message_box('Game over', 'Play again?')
                serpent.reset((10,10))
                break
                
        redraw_window(window, rows, width, serpent, snack)
                
    
def set_cube_size(rows, height, width):
    Cube.rows = rows
    Cube.height = height
    Cube.width = width
    
    
if __name__ == "__main__":
    # Rows are an integer count
    # width, height are in pixels
    rows = 10
    screen_width = 500
    screen_height = 500
    
    set_cube_size(rows, screen_width, screen_height)         
    main(rows, screen_width, screen_height)     