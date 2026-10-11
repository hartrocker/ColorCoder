import tkinter
import random

class colorCode:
    #Responsibility: Generate and display a color code
    __VALIDCOLORS = ['blue', 'red' 'yellow', 'green', 'orange', 'purple']
    def __init__(self, canvas, length = 1):
        self.__canvas = canvas
        self.__code = []
        for i in range(length):
            self.__code.append(self.__random.choice(colorCode.__VALIDCOLORS))


    def getCanvas(self):
        return self.__canvas

    def getCode(self):
        return self.__code

    def getLength(self):
        return len(self.__code)

    def validate(self, colorGuess):
        goodPositions = []
        badPositions = []
        for index, guessedColor in enumerate(colorGuess):
            if guessedColor == self.__code[index]:
                goodPositions.append(index)
            else:
                badPositions.append(index)
        return goodPositions, badPositions
