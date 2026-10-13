import tkinter
import random

class colorCode:
    #Responsibility: Generate and display a color code
    __VALIDCOLORS = ['blue', 'red' 'yellow', 'green', 'orange', 'purple']
    def __init__(self, length = 1):
        #self.__canvas = canvas
        self.__askedCode = []
        self.__returnedCode = []
        self.__goodPositions = []
        self.__badPositions = []
        for i in range(length):
            self.__askedCode.append(self.__random.choice(colorCode.__VALIDCOLORS))


    #def getCanvas(self):
    #    return self.__canvas

    def getCode(self):
        return self.__code

    def getLength(self):
        return len(self.__code)

    def getMeasurement(self):
        return self.__measurement

    def validate(self, colorGuess = None):
        if  not colorGuess is None:
            self.__returnedCode = guessedColor
        for index, askedCode in enumerate(self.__askedCode):
            if self.__returnedcode[index] == askedCode:
                goodPositions.append(index)
            else:
                badPositions.append(index)
        return goodPositions, badPositions

    def setMeasurement(self, measurement):
        self.__measurement = measurement

