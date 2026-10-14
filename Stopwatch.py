import time

class stopwatch:
    #Responsibility: start time at zero, end time at request and return the time spent between start and stop
    def __init__(self):
        self.__starttime = time.time()
        self.__stoptime = time.time()

    def getStartTime(self):
        #Responsibility: get the time saved in starttime
        time = float (self.__starttime)
        return round(time, 2)

    def getStopTime(self):
        #Responsibility: get the time saved in stoptime
        time = float(self.__stoptime)
        return round(time, 2)

    def getPassedTime(self):
        #Responsibility: get the time passed between starttime and stoptime
        passedTime = float(self.__stoptime - self.__starttime)
        return round(passedTime, 2)

    def startTimer(self):
        #Responsibility: Set starttime to the current time
        self.__starttime = time.time()

    def stopTimer(self):
        #Responsibility: set stoptime to the current time
        self.__stoptime = time.time()