from Measurement import measurement
from ColorCode import colorCode

class experiment():
    def __init__(self):
        self.__testedCodes = []

    def getCodes(self):
        return self.__testedCodes

    def addCode(self, code):
        self.__testedCodes.append(colorCode)

    def getExperimentLength(self):
        return len(self.__testedCodes)

    def getLastMeasurement(self):
        return self.__testedCodes[len(self.__testedCodes) - 1]




