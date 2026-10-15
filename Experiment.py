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
        self.__curentMeasurement = measurement

    def getMeasurements(self):
        #Responsibility: Return all measurements as list
        return self.__testMeasurements

    def addMeasurement(self, measurement):
        #Responsibility: add a measurement to the collection of measurements
        self.__testMeasurements.append(measurement)

    def getExperimentLength(self):
        #Responsibility: Get the amount of measurements that have been registered
        return len(self.__testMeasurements)

    def getLastMeasurement(self):
        #Responsibility: get the last measurement in the list
        return self.__testMeasurements[len(self.__testMeasurements) - 1]

    def getLastGuessTime(self):
        # Responsibility: get the guesstime for the last measurement in the list
        return self.__testMeasurements[len(self.__testMeasurements) - 1].getTimeResponse()

    def getLastShowTime(self):
        # Responsibility: get the showtime for the last measurement in the list
        return self.__testMeasurements[len(self.__testMeasurements) - 1].getTimeShowed()

    def getLastResult(self):
        # Responsibility: get the result for the last measurement in the list
        # Result is True for no errors, False for Errors
        measurement = self.getLastMeasurement()
        return measurement.getResult()

    def getLastLength(self):
        # Responsibility: get the length of the last colorcode in the list
        if self.__testMeasurements:
            measurement = self.getLastMeasurement()
            print("Measurement exists. length is ", measurement.getLength())
            return measurement.getLength()
        else:
            print("Measurement does not exist")
            return 0

    def startMeasurement(self):
        # Responsibility: start a new measurement. harder if the last one was error free, easier if not
        self.__screen.disableGuessing()
        if len(self.__testMeasurements) == 0:
            code = colorCode(length=3)
            showTime = 5
        elif len(self.__testMeasurements) > 0:
            timerAdjustment=randint(0,99)
            timerAdjustment=float(timerAdjustment/100)
            print("the last result was ", self.getLastResult())
            if self.getLastResult() == True:
                showTime = self.getLastShowTime()-timerAdjustment
                codelength = self.getLastLength()+1
                print("codelength now is ", codelength)
            elif self.getLastResult() == False:
                showTime = self.getLastShowTime()+timerAdjustment
                codelength = self.getLastLength()-1
                print("codelength now is ", codelength)
            code = colorCode(length=codelength)
        startedMeasurement = measurement(time = showTime)
        startedMeasurement.setAskedCode(code=code)
        self.__testMeasurements.append(startedMeasurement)
        screen = self.__screen.getScreen()
        code.draw(canvas=screen)
        showTime=int(showTime*1000)
        screen.after(showTime, code.undraw)
        screen.after(showTime, self.__timer.startTimer)
        screen.after(showTime, self.__screen.enableGuessing)


    def setGuessedCode(self, code):
        #Responsibility: append the guessed code to the measurment
        inputCode = colorCode(colorlist=code)
        measurement = self.getLastMeasurement()
        measurement.setGuessedCode(guessedCode=inputCode)

    def stop(self):
        #Responsibility: stop the timer, get the time and add the guesstime to the experiment
        self.__timer.stopTimer()
        passedTime = self.__timer.getPassedTime()
        measurement = self.getLastMeasurement()
        measurement.setTimeResponse(passedTime)

    def displayPercentage(self):
        #Responsibility: For all measurements in experiment, show the succesrate
        for measurement in self.__testMeasurements:
            print("Experiment was ", measurement.getPercentageRight(), "right")

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
