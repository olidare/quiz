import pygame
import time
from game import Game
from button import *
from leaderboard import Leaderboard
from layout import Layout

class Main:
    dw, dh = 1380,1000
    gameDisplay = pygame.display.set_mode((dw, dh))
    clock = pygame.time.Clock()
    backgroundColour = (30, 144, 255)
    yellow, light_yellow = (200,200,0), (255,255,0)
    red,bright_red = (200, 0, 0), (255, 0, 0)
    green, bright_green = (0, 200, 0), (0, 255, 0)
    lb = Leaderboard()
    layout = Layout()
    button = Button()
    game = Game()

    def quitgame(self):
        pygame.quit()
        quit()

    def start_game(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitgame()

            self.main_setup()
            self.clock.tick(15)

    def game_instructions(self):
        gcont = True
        while gcont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitgame()

            self.intro_setup()
            self.clock.tick(15)


    def main_setup(self):
        self.gameDisplay.fill(self.backgroundColour)
        self.layout.message_Title("Welcome to the ", (self.dw / 2), (self.dh * 2 / 8), 50)
        self.layout.message_Title("Charity Quiz Game!", (self.dw / 2), (self.dh * 3 / 8), 50)

        self.button.button(self.gameDisplay, "Start Game!", (self.dw * 1 / 8), (self.dh * 0.75), 150, 50, self.green,
                           self.bright_green, self.game.game_loop)
        self.button.button(self.gameDisplay, "Leaderboard", (self.dw * 3 / 8), (self.dh * 0.75), 150, 50, self.green,
                           self.bright_green, self.lb.leader_board)
        self.button.button(self.gameDisplay, "Instructions", (self.dw * 5 / 8), (self.dh * 0.75), 150, 50, self.green,
                           self.bright_green, self.game_instructions)
        self.button.button(self.gameDisplay, "Quit", (self.dw * 7 / 8), (self.dh * 0.75), 80, 50, self.red, self.bright_red,
                           self.quitgame)
        pygame.display.update()


    def intro_setup(self):
        self.gameDisplay.fill(self.backgroundColour)
        self.layout.message_Title("Instructions: ", (self.dw / 2), (self.dh * 1 / 9), 55)
        self.layout.message_Title(":- Multiple choice quiz game, controlled by keys 1-4.", (self.dw / 2),
                                  (self.dh * 2 / 9), 25)
        self.layout.message_Title(":- Game ends when lives run out, lives are lost if a normal blue question is answered wrong", (self.dw / 2),
                                  (self.dh * 3 /9 ), 25)
        self.layout.message_Title(":- 25 seconds to answer each normal question and points can be gained for speed. ", (self.dw / 2),
                                  (self.dh * 4 / 9), 25)
        self.layout.message_Title(":- Red Background indicates it's a bonus question", (self.dw / 2),
                                  (self.dh * 5 / 9), 25)
        self.layout.message_Title(":- Lives and points are not lost for Bonus Questions", (self.dw / 2),
                                  (self.dh * 6 / 9), 25)
        self.layout.message_Title(":- Bonus Questions in red are designed for raising charity awareness", (self.dw / 2),
                                  (self.dh * 7 / 9), 25)
        self.button.button(self.gameDisplay, "Main", (self.dw * 2 / 8), (self.dh * 0.85), 150, 50,
                           self.yellow,
                           self.light_yellow, self.start_game)
        self.button.button(self.gameDisplay, "quit", (self.dw * 5 / 8), (self.dh * 0.85), 150, 50, self.red,
                           self.bright_red,
                           self.quitgame)
        pygame.display.update()


pygame.init()
pygame.display.set_caption(' Quiz')

#To run code without linking it to arduino
run = Main()
run.start_game()
