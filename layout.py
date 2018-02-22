from textWrapper import TextRectException
import pygame
import time
from button import Button

class Layout:
    dw, dh = 1380,1000
    backgroundColour = (30, 144, 255)
    yellow = (255, 255, 0)
    green, bright_green = (0, 200, 0), (0, 255, 0)
    red,bright_red = (200, 0, 0), (255, 0, 0)
    gameDisplay = pygame.display.set_mode((dw, dh))
    button = Button()
    textWrap = TextRectException()

    #Puts all of the 4 answers into 4 different textboxes and draws borders around them
    def answer1(self,text, colour):
        self.button.button(self.gameDisplay, "1: ", (self.dw * 0.15), (self.dh * 0.5), 60, 50, self.green, self.bright_green,None)
        self.textBox(self.gameDisplay, self.bright_green, (self.dw * 0.22), (self.dh * 0.5), (self.dw * 0.28),(self.dh * 0.25))
        self.questionBox(text,(self.dw * 0.23), (self.dh * 0.51), (self.dw * 0.27), (self.dh * 0.24), 25, colour)

    def answer2(self,text, colour):
        self.button.button(self.gameDisplay,"2: ", (self.dw * 0.52), (self.dh * 0.5), 60, 50, self.green, self.bright_green,None)
        self.textBox(self.gameDisplay, self.bright_green, (self.dw * 0.6), (self.dh * 0.5), (self.dw * 0.28),(self.dh * 0.25))
        self.questionBox(text,(self.dw * 0.61), (self.dh * 0.51), (self.dw * 0.27), (self.dh * 0.23), 25, colour)

    def answer3(self,text, colour):
        self.button.button(self.gameDisplay,"3: ", (self.dw * 0.15), (self.dh * 0.75), 60, 50, self.green, self.bright_green,None)
        self.textBox(self.gameDisplay, self.bright_green, (self.dw * 0.22), (self.dh * 0.75), (self.dw * 0.28),(self.dh * 0.24))
        self.questionBox(text,(self.dw * 0.23), (self.dh * 0.76), (self.dw * 0.27), (self.dh * 0.22), 25, colour)

    def answer4(self,text, colour):
        self.button.button(self.gameDisplay,"4: ", (self.dw * 0.52), (self.dh * 0.75), 60, 50, self.green, self.bright_green,None)
        self.textBox(self.gameDisplay, self.bright_green, (self.dw * 0.6), (self.dh * 0.75), (self.dw * 0.28),(self.dh * 0.24))
        self.questionBox(text,(self.dw * 0.61), (self.dh * 0.76), (self.dw * 0.27), (self.dh * 0.22), 25, colour)

    #Puts the question, answers, lives and score on the pygame display
    def questionandAnswers(self, Question, a,b,c,d, lives,finalScore,time, colour):
        self.gameDisplay.fill(colour)
        self.questionBox(Question, (self.dw / 4), (self.dh / 8), (self.dw * 0.6), (self.dh * 0.35), 40, colour)
        self.answer1(a, colour)
        self.answer2(b, colour)
        self.answer3(c, colour)
        self.answer4(d, colour)
        self.lives_remaining(lives)
        self.score(finalScore)
        self.timing(time)
        pygame.display.update()

    def score(self, score):
        my_font = pygame.font.Font("Quicksand-Regular.otf", 32)
        text = my_font.render("Score: " + str(score), True, self.yellow)
        self.gameDisplay.blit(text, [0, 0])

    def timing(self, time):
        my_font = pygame.font.Font("Quicksand-Regular.otf", 32)
        text = my_font.render("Time: " + str(time), True, self.yellow)
        self.gameDisplay.blit(text, [(0.5*self.dw), 0])
        pygame.display.update()

    def lives_remaining(self, lives):
        my_font = pygame.font.Font("Quicksand-Regular.otf", 32)
        text = my_font.render("Lives: " + str(lives), True, self.yellow)
        self.gameDisplay.blit(text, [(0.85*self.dw), 0])

    def questionBox(self,text, x,y,w,h, font_size, colour):
          my_font = pygame.font.Font("Quicksand-Regular.otf", font_size)
          my_rect = pygame.Rect(x,y,w,h)
          rendered_text = self.textWrap.render_textrect(text, my_font, my_rect, self.yellow, colour, 0)
          self.gameDisplay.blit(rendered_text, my_rect.topleft)

    def textBox(self,screen, colour,x,y,h,w):
        thickness = 2
        pygame.draw.rect(screen, colour, (x,y, h, w),thickness)

    def correct(self,string):
        self.message_display(string)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.yellow)
        return textSurface, textSurface.get_rect()

    #Message pops up for a certain amount of time
    def message_display(self, text, display_length, text_size):
        largeText = pygame.font.SysFont("monospace", text_size)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((self.dw / 2), (self.dh * 0.45))
        self.gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(display_length)
        self.gameDisplay.fill(self.backgroundColour)

    #Used for headers and titles
    def message_Title(self, text, x, y, text_size):
        largeText = pygame.font.SysFont("monospace", text_size)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((x), (y))
        self.gameDisplay.blit(TextSurf, TextRect)


