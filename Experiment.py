from Measurement import measurement
from ColorCode import colorCode
from Stopwatch import stopwatch
from random import randint
from Scatterplot import scatterplot

class experiment():
    def __init__(self, canvas):
        self.__testMeasurements = []
        self.__screen = canvas
        self.__timer = stopwatch()
        self.__previousMeasurement = None
        self.__currentMeasurement = measurement

    def getMeasurements(self):
        #Responsibility: Return all measurements as list
        return self.__testMeasurements

    def getCurrentMeasurement(self):
        return self.__currentMeasurement

    def getPreviousMeasurement(self):
        return self.__previousMeasurement

    def addMeasurement(self, measurement):
        #Responsibility: add a measurement to the collection of measurements
        self.__testMeasurements.append(self.__currentMeasurement)

    def getNrOfMeasurements(self):
        #Responsibility: Get the amount of measurements that have been registered
        return len(self.__testMeasurements)

    def adjustMeasurementParameters(self):
        timerAdjustment = randint(0, 99)
        timerAdjustment = float(timerAdjustment / 100)
        if self.__previousMeasurement.getResult() == True:
            showTime = self.__previousMeasurement.getTimeShowed() - timerAdjustment
            codelength = self.__previousMeasurement.getLength() + 1
            print("codelength now is ", codelength)
        elif self.__previousMeasurement.getResult() == False:
            showTime = self.__previousMeasurement.getTimeShowed() + timerAdjustment
            codelength = self.__previousMeasurement.getLength() - 1
            print("codelength now is ", codelength)
            if codelength < 3:
                codelength = 3
            if showTime < 2:
                showTime =2
        return showTime, codelength

    def startMeasurement(self):
        # Responsibility: start a new measurement. harder if the last one was error free, easier if not
        self.__screen.disableGuessing()
        if self.__previousMeasurement == None:
            code = colorCode(length=3)
            showTime = 5
        else:
            showTime, codelength = self.adjustMeasurementParameters()
            code = colorCode(length=codelength)
        self.__currentMeasurement = measurement(time = showTime)
        self.__currentMeasurement.setAskedCode(code = code)
        #self.__testMeasurements.append(startedMeasurement)
        screen = self.__screen.getScreen()
        code.draw(board=self.__screen)
        showTime=int(showTime*1000)
        screen.after(showTime, lambda:code.undraw(board=self.__screen))
        screen.after(showTime, self.__timer.startTimer)
        screen.after(showTime, self.__screen.enableGuessing)

    def setGuessedCode(self, code):
        #Responsibility: append the guessed code to the measurment
        inputCode = colorCode(colorlist=code)
        self.__currentMeasurement.setGuessedCode(guessedCode=inputCode)

    def stopTime(self):
        #Responsibility: stop the timer, get the time and add the guesstime to the experiment
        self.__timer.stopTimer()
        passedTime = self.__timer.getPassedTime()
        self.__currentMeasurement.setTimeResponse(passedTime)
        if self.__currentMeasurement.validateMeasurement():
            self.__previousMeasurement = self.__currentMeasurement
            self.__testMeasurements.append(self.__currentMeasurement)
            self.__currentMeasurement = measurement()

    '''
    def displayPercentage(self):
        #Responsibility: For all measurements in experiment, show the succesrate
        for measurement in self.__testMeasurements:
            print("Experiment was ", measurement.getPercentageRight(), "right")
    '''

    def ScatterData(self, dataX, dataY):
        xDataList = []
        yDataList = []
        if dataX =='codeLength' and dataY =='percentRight':
            for measurement in self.__testMeasurements:
                xDataList.append(measurement.getLength())
                yDataList.append(measurement.getPercentageRight())
            title = "Succesrate for length"
        elif dataX =='showTime' and dataY =='percentRight':
            for measurement in self.__testMeasurements:
                xDataList.append(measurement.getTimeShowed())
                yDataList.append(measurement.getPercentageRight())
            title = "Succesrate for time shown"
        plot = scatterplot(xAxis=dataX, yAxis=dataY, x=xDataList, y=yDataList, title=title)
        plot.drawPlot()
