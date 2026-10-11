import time

class stopwatch:
    #Responsibility: start time at zero, end time at request and return the time spent between start and stop
    def __init__(self):
        self.__starttime = time.time()
        self.__stoptime = time.time()

    def getStartTime(self):
        return self.__starttime

    def getStopTime(self):
        return self.__stoptime

    def getPassedTime(self):
        passedTime = int(self.__stoptime - self.__starttime)
        return round(passedTime, 2)

    def startTimer(self):
        self.__starttime = time.time()

    def stopTimer(self):
        self.__stoptime = time.time()