from random import shuffle
import collections


class FileRead:
    filename = ""

    #this function reads .txt file into a dictionary
    def readText(self):
        QandA = collections.OrderedDict()
        numberofLines = 0
        with open(self.filename, "r") as readfile:
            for line in readfile:
                numberofLines += 1
                content = line.split("`") #splits the lines with "`"
                question = content[0] #first split is always the question
                answers = []
                #for the second to fifth splits, they are appended to a list
                for index, line in enumerate(content):
                    if (index >= 1 and index <5):
                        answers.append(line)
                    #Question and the list of answers are updated to an empty QandA dictionary
                    QandA.update({question: answers})
            return QandA, numberofLines

    #simple fileread which appends a .txt file to a list
    def readFact(self):
        facts = []
        with open(self.filename, "r") as readfile:
            for line in readfile:
                content = line.split("`")
                for c in content:
                    facts.append(c)
        shuffle(facts)
        return facts[0] #function returns a random fact every time.


