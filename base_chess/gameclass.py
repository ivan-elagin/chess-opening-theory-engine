import pygame
from base_chess.constants import *

class Game:
    def __init__(self):
        pass
    
    # This show method will be called in the mainloop of the main.py file
    
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) # light green  
                else:
                    color = (119, 154, 88) # dark green
                    
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                
                pygame.draw.rect(surface, color, rect)
                