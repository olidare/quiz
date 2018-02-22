from fileread import FileRead
from random import shuffle
from layout import Layout
import time
import random
import pygame

class Question:
    backgroundColour, backgroundBonus = (30, 144, 255), (220,20,60)
    layout = Layout()
    mainQuiz = FileRead()
    mainQuiz.filename = "testfile.txt"
    attemptMain, mainLength = mainQuiz.readText()
    bonusQuiz = FileRead()
    bonusQuiz.filename = "bonus.txt"
    attemptBonus, bonusLength = bonusQuiz.readText()
    clock = pygame.time.Clock()

    # Function for creating the standard questions
    def normal(self, list, finalScore, question_count, lives):
        for i in list:
            question_count += 1
            count, questionMain, answersMain, correctAnswerMain, \
            rand1, rand2 = self.initialise_normal(i)
            while (count > 0):
                count -= 1
                finalScore -=3
                userAnswer = self.controls()
                # finds the index of where the correct answer is placed
                answersMainIndex = (1 + answersMain.index(correctAnswerMain))
                self.clock.tick(30)
                if (userAnswer != None):
                    print("answersmain index is : " +str(answersMainIndex))
                    if (int(userAnswer) == int(answersMainIndex)):
                        self.layout.message_display("Correct", 1, 60)
                        finalScore += 2500
                        break
                    else:
                        self.layout.message_display("Incorrect, answer was: " + str(correctAnswerMain), 5, 30)
                        finalScore -= 100
                        lives -=1
                        return finalScore, question_count, lives
                # puts the questions and answers into layout class to be displayed in game
                if (count%25==0):
                    self.layout.questionandAnswers(questionMain, answersMain[0], answersMain[1], answersMain[2],
                                                   answersMain[3], lives, finalScore,self.time_convert(count),
                                                   self.backgroundColour)
                if (count == 0):
                    self.layout.message_display("Took too long, answer was: " + str(correctAnswerMain), 5, 30)
                    lives -= 1
                    break

        return  finalScore, question_count, lives

    # Function for creating the bonus questions
    def bonus(self, bonuspoints, finalScore, lives):
        for b in bonuspoints:
            count, questionBonus, answersBonus, \
            correctAnswerBonus = self.initialise_bonus(b)
            while (count > 0):
                count -= 1
                userAnswer = self.controls()
                # finds the index of where the correct answer is placed
                answersMainIndex = (1 + answersBonus.index(correctAnswerBonus))
                self.clock.tick(30)
                if (userAnswer != None):
                    #if user input matches correct answer
                    if (int(userAnswer) == int(answersMainIndex)):
                        self.layout.message_display("Correct", 1, 60)
                        finalScore += 5000
                        break
                    else:
                        self.layout.message_display("Incorrect, answer was: " + str(correctAnswerBonus), 5, 30)
                        break
                if (count%25==0):
                    # puts the questions and answers into layout class to be displayed in game
                    self.layout.questionandAnswers(questionBonus, answersBonus[0], answersBonus[1], answersBonus[2],
                                                   answersBonus[3], lives, finalScore, self.time_convert(count),
                                                   self.backgroundBonus)
        return finalScore

    #returns a corresponding value depending on key pressed
    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return '1'
                elif event.key == pygame.K_2:
                    return '2'
                elif event.key == pygame.K_3:
                    return '3'
                elif event.key == pygame.K_4:
                    return '4'

    def randomiseList(self, x):
        list = random.sample(xrange(0, x), x-1)
        return list

    #selects a specific number of values to be used in a list
    def selectedRange(self, list, start, end):
        updatedList = []
        for m in list[start: end]:
            updatedList.append(m)
        return updatedList

    def clearValues(self, list, list2):
        del list[:]
        del list2[:]

    def time_convert(self, time):
        converted_vale = time/30
        return converted_vale

    def fifty_fifty(self, answersMain, value1, value2):
        answersMain[value1] = ""
        answersMain[value2] = ""


    def initialise_normal(self, i):
        count = 750
        questionMain = self.attemptMain.keys()[i - 1]  # Extracts the Question from the Dictionary
        answersMain = (self.attemptMain.values()[i - 1])  # Extracts the answers from the Dictionary
        correctAnswerMain = answersMain[0]  # records the correct answer
        random1 = answersMain[1]
        random2 = answersMain[2]
        shuffle(answersMain)
        rand1 = (answersMain.index(random1))
        rand2 = (answersMain.index(random2))
        return count, questionMain, answersMain, correctAnswerMain, int(rand1), int(rand2)

    def initialise_bonus(self, b):
        count = 1000
        questionBonus = self.attemptBonus.keys()[b - 1]  # Extracts the Question from the Dictionary
        answersBonus = self.attemptBonus.values()[b - 1]  # Extracts the answers from the Dictionary
        correctAnswerBonus = answersBonus[0]  # records the correct answer
        shuffle(answersBonus)
        return count, questionBonus, answersBonus, correctAnswerBonus