from ColorCode import colorCode

class measurement:
    __VALIDCOLORS = ['blue', 'red' 'yellow', 'green', 'orange', 'purple']
    def __init__(self, length, displayTime):
        self.__askedCode = []
        self.__returnedCode = []
        self.__goodPositions = []
        self.__badPositions = []
        self.__displayTime = displayTime

        for i in range(length):
            self.__askedCode.append(self.__random.choice(colorCode.__VALIDCOLORS))

    def getDisplayTime(self):
        return self.__DisplayTime

    def getReactionTime(self):
        return self.__reactionTime

    def setReactionTime(self, time):
        self.__reactionTime = time

    #def getCanvas(self):
    #    return self.__canvas

    def getAskedCode(self):
        return self.__askedCode

    def getReturnedCode(self):
        return self.__returnedCode

    def getLength(self):
        return len(self.__askedCode)

    def getMeasurement(self):
        return self.__measurement

    def setReturnCode(self, code):
        self.__returnedCode = code

    def validate(self):
        for index, askedCode in enumerate(self.__askedCode):
            if self.__returnedcode[index] == askedCode:
                self.__goodPositions.append(index)
            else:
                self.__badPositions.append(index)
        return self.__goodPositions, self.__badPositions

    def setMeasurement(self, measurement):
        self.__measurement = measurement

    def getResult(self):
        result = self.getLength() - self.__badPositions






