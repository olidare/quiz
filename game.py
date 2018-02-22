import pygame
import random
import inputbox
import time
from questions import Question
from layout import Layout
from leaderboard import Leaderboard
from fileread import FileRead
from button import Button

class Game:
    dw, dh = 1380,1000
    backgroundColour, backgroundBonus = (30, 144, 255), (220,20,60)
    yellow, bright_red = (255, 255, 0), (255, 0, 0)
    green, bright_green = (0, 200, 0), (0, 255, 0)
    finalScore = 3000
    question_count = 0
    lives = 3
    gameDisplay = pygame.display.set_mode((dw, dh))
    clock = pygame.time.Clock()
    question = Question()
    layout = Layout()
    lb = Leaderboard()
    button = Button()

    def game_loop(self):
        #initialises the original scores
        gameExit, self.lives = False, 3
        mainIndex, bonusIndex, selectedQuestions,\
        selectedBonus, mainFreq, bonusFreq = self.initialiseGame()
      #  self.getRandomFact()
        while not gameExit:
            self.respawnValues()
            if ((self.lives == 0)): #if out of lives, game over
                self.verifyScore()
                break
            if (self.question_count >20): #if completed all of the questions, game over
                self.layout.message_display("Congratulations, you've completed the quiz! finalscore is: "
                                            + str(self.finalScore), 8, 30)
                self.verifyScore()
                break
            else:
                self.getNextQuestion(selectedQuestions) #Else load more normal questions
                if(self.lives > 0):
                    self.getBonus(selectedBonus) #load a bonus question if lives still remain
                else:
                    self.verifyScore() #if no lives remain, compare score to existing leaderboard scores
                    break
            #This updates all of the information so more questions can be loaded
            mainFreq, bonusFreq, mainIndex, bonusIndex, selectedQuestions, selectedBonus = \
                self.updateValues(mainFreq, bonusFreq, mainIndex, bonusIndex, selectedQuestions, selectedBonus)
        self.post_game()

    #Screen after completing game, there is no button to play another round
    def post_game(self):
        gcont = True
        while gcont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitgame()

            self.post_game_screen()
            self.clock.tick(15)


    def post_game_screen(self):
        self.gameDisplay.fill(self.backgroundColour)

        self.layout.message_Title("Thanks for donating", (self.dw / 2), (self.dh * 2 / 8), 50)
        self.layout.message_Title("and playing!", (self.dw / 2), (self.dh * 3 / 8), 50)
        self.button.button(self.gameDisplay, "Leaderboard", (self.dw * 2 / 8), (self.dh * 0.85), 150, 50,
                           self.green,
                           self.bright_green,  self.lb.leader_board)
        self.button.button(self.gameDisplay, "quit", (self.dw * 5 / 8), (self.dh * 0.85), 150, 50, self.bright_red,
                           self.bright_red,
                           self.quitgame)
        pygame.display.update()



    def updateValues(self, mainFreq, bonusFreq, mainIndex, bonusIndex, selectedQuestions, selectedBonus):

        #removes previous indexes in the list
        self.question.clearValues(selectedQuestions, selectedBonus)

        #moves indexes along the dictionary so they ask the next questions in order
        mainStart = mainFreq
        mainFreq = mainFreq + random.randint(3,5) #will be a random number of questions between 3 and 5
        bonusStart = bonusFreq
        bonusFreq += 1

        selectedQuestions = self.question.selectedRange(mainIndex, mainStart, mainFreq)
        selectedBonus = self.question.selectedRange(bonusIndex, bonusStart, bonusFreq)

        return  mainFreq, bonusFreq, mainIndex, bonusIndex, selectedQuestions, selectedBonus

    #calls the next standard questions
    def getNextQuestion(self, selectedQuestions):
        self.layout.score(self.finalScore)
        self.layout.lives_remaining(self.lives)
        self.finalScore, self.question_count, self.lives = self.question.normal(selectedQuestions, self.finalScore,
                                                                                self.question_count, self.lives)
    #gets a fact for the start of the game by reading a .txt file
    def getRandomFact(self):
        rfact = FileRead()
        rfact.filename = "fact.txt"
        randomValue = rfact.readFact()

        self.gameDisplay.fill(self.backgroundColour)
        #insert a fact from the fact.txt file into the display text box
        self.layout.questionBox(randomValue, (self.dw / 4), (self.dh / 8),
                                (self.dw * 0.6), (self.dh * 0.65), 40, self.backgroundColour)
        pygame.display.update()
        time.sleep(7)

    def initialiseGame(self):
        mainStart, bonusStart, bonusFreq = 0, 0, 1
        mainFreq = random.randint(3, 5)

        #randomises the indexes of the Dictionary
        mainIndex = self.question.randomiseList(self.question.mainLength)
        bonusIndex = self.question.randomiseList(self.question.bonusLength)

        #gets a selected range of questions
        selectedQuestions = self.question.selectedRange(mainIndex, mainStart, mainFreq)
        selectedBonus = self.question.selectedRange(bonusIndex, bonusStart, bonusFreq)

        return  mainIndex, bonusIndex, selectedQuestions, selectedBonus, mainFreq, bonusFreq

    def respawnValues(self):
        self.gameDisplay.fill(self.backgroundColour)
        self.layout.score(self.finalScore)
        self.layout.lives_remaining(self.lives)

    #calls the bonus questions
    def getBonus(self, selectedBonus):
        self.gameDisplay.fill(self.backgroundColour)
        self.layout.message_display("Bonus Question", 1, 60)
        self.gameDisplay.fill(self.backgroundBonus)
        self.finalScore = self.question.bonus(selectedBonus, self.finalScore, self.lives)

    #If score is higher than the lowest value in the leaderboard, ask for username
    def verifyScore(self):
        if (self.finalScore > self.lb.smallest_value):
            self.new_highscore(self.finalScore)


    def new_highscore(self, finalscore):
        #Gets username
        username = inputbox.ask(self.gameDisplay,
                                'New highscore, enter username: ')
        #puts username and score into leaderboard
        self.lb.updated_leaderboard(self.lb.df, username, self.finalScore)

    def quitgame(self):
        pygame.quit()
        quit()
