from ColorCode import colorCode

class measurement:
    def __init__(self, time = None, length = None):
        self.__timeShowed = time
        self.__timeResponse = None
        self.__exampleCode = colorCode(length)
        self.__guessedCode = None
        self.__goodPositions = []
        self.__badPositions = []

    def getExampleCode(self):
        #Responsibility: get the color code that was displayed on screen
        return self.__exampleCode.getCode()

    def getGuessedCode(self):
        #Responsibility: get the color code that the user entered
        return self.__guessedCode.getCode()

    def getTimeShowed(self):
        #Responsibility: return the time the color code for this measurement was displayed on screen
        return self.__timeShowed

    def getTimeGuessed(self):
        #Responsiblitiy: return the time it took the user to enter the guessed code
        return self.__timeResponse

    def getNrGoodpositions(self):
        #Responsibility: Return the number of colors/positions that the user got right in this code
        return len(self.__goodPositions)

    def getNrBadPositions(self):
        #Responsibility: Return the number of colors/positions that the user got wrong in this code
        return len(self.__badPositions)

    def getLength(self):
        #Responsiblity: Return how long the current code is
        return len(self.__exampleCode.getCode())

    def getResult(self):
        #Responsibility: Return true there are no badpositions, false if there are badpositions
        if self.__badPositions:
            return False
        else:
            return True

    def getPercentageRight(self):
        #Responsibitity: Return the percentage of colors/positions that have been entered correctly
        result = self.getNrGoodpositions()/self.getLength()*100
        return result

    def setTimeShowed(self, time):
        #Responsibility: store the time this code was showed on screen
        self.__timeShowed = time

    def setTimeResponse(self, time):
        #Responsibility: store the time it took the user to guess this code
        self.__timeResponse = time

    def setAskedCode(self, code):
        #Responsibility: store the code that has been generated
        self.__exampleCode = code

    def setGuessedCode(self, guessedCode):
        #Responsibility: store the code that was guessed in the measurement
        #Responsibility: call setGoodBad so the results get processed
        self.__guessedCode = guessedCode
        self.setGoodBad()

    def setGoodBad(self):
        #Responsibility: for each color, check if it was right or wrong. append the index to goodPositions or badPostions accordingly
        for index, color in enumerate(self.__exampleCode.getCode()):
            guessedCode = self.__guessedCode.getCode()
            if color == guessedCode[index]:
                self.__goodPositions.append(index)
            else:
                self.__badPositions.append(index)
        self.showMeasurement()

    def showMeasurement(self):
        print("everything processed")
        print("example code: ", self.__exampleCode.getCode())
        print("guessed code: ", self.__guessedCode.getCode())
        print("good positions: ", len(self.__goodPositions))
        print("bad positions: ", len(self.__badPositions))
        print("showtime: ", self.getTimeShowed())
        print("guesstime: ", self.getTimeGuessed())

    def validateMeasurement(self):
        valid=True
        if not type(self.__exampleCode) == colorCode or not type(self.__guessedCode) == colorCode:
            print ("The code(s) are not a colorCode")
            example = type(self.__exampleCode)
            guessed = type(self.__guessedCode)
            print("Example code is ", example, "Guessed code is ", guessed, "")
            valid = False
        elif not self.__timeShowed > 0 or not self.__timeResponse > 0:
            print("Times do not contain valid numbers")
            valid = False
        elif (len(self.__badPositions) + len(self.__goodPositions) != self.__exampleCode.getLength()):
            print("Not enough positions were guessed correctly or incorrectly")
            valid = False
        return valid

if __name__ == '__main__':
    import pytest
    pytest.main(['measurementTest.py', '--cov=Measurement', '--cov-report=term-missing'])