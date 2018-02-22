''' This class taken from Stack Overflow, code made by Timothy Downs

This class opens a screen which allows the user to enter information
into a textbox and the data is recorded as a string which can then be
used elsewhere.

In this case, it is used to record a username for the leaderboard.
'''

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

backgroundColour = (30, 144, 255)
yellow = (255, 255, 0)

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
        return event.key
    else:
        pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  font = pygame.font.Font(None,24)

  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 3), (screen.get_height() / 3), 400,80), 0)

  pygame.draw.rect(screen, (backgroundColour),
                   ((screen.get_width() / 3),(screen.get_height() / 3), 408,96), 1)
  if len(message) != 0:
    screen.blit(font.render(message, 1, (yellow)),
                ((screen.get_width() / 3 +5), (screen.get_height() / 3) + 10))

  pygame.display.flip()



def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def main():
  screen = pygame.display.set_mode((1200,900))
  print ask(screen, "UserName") + " was entered"
  #main.game_intro()



