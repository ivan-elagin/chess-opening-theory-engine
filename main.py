"""
    OPENING THEORY TOOL
    -------------------
    
    The goal of this project is to provide an efficient and helpful tool for learning chess openings theory.
    A chess opening is a sequence of moves that is played at the beginning of a game. 
    It is usually a good idea to follow a well-known opening because it has been studied and played by many people before. 
    This allows you to avoid traps and to reach a good position in the middlegame.
    
    The user can select the opening they want to learn and the tool with provide them with the moves
    and comments for each move. The user can also play the moves on the board and see the evaluation of the position.
    
    I hope this tool can help beginners and intermediate players to learn and understand the openings better. Try it out and enjoy the game!
    
"""

import pygame
import sys
from base_chess.constants import *
from base_chess.gameclass import Game

class Main:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Chess Opening Theory Tool')
        self.game = Game()

    def mainloop(self):
        
        while True:
            self.game.show_bg(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.update()

main = Main()
main.mainloop()
