from tkinter import *
from Experiment import experiment
from Measurement import measurement

class board(Canvas):
    #Responsibility: Set a field for balls to move on, and set the balls in motion when controls are pressed to do so
    #Also, keep track of the statusMoving: are the balls in a continuous state of motion
    def __init__(self, root):
        window = root
        window.title("Color guessing game!")
        self.__result = []
        self.__guessing = False
        self.__experiment = experiment(canvas=self)

        self.__canvas = Canvas(window, width=600, height=300, background="lightyellow")

        #Top menu items
        btn_frame = Frame(window)  # for layouting row of draw buttons
        self.createLabel(btn_frame, "Menu ")
        self.createButton(btn_frame, "New code", self.startTest)
        self.createButton(btn_frame, "size-succes", self.showResults)
        self.createButton(btn_frame, "showtime-succes", self.showTimeResults)

        #Color input menu
        color_frame = Frame(window)
        #why can't I use a variable when calling the click_action... would make appending colors so much easier
        self.createButton(color_frame, "", click_action = lambda:self.submitColor("yellow"), btncolor="yellow")
        self.createButton(color_frame, "", click_action = lambda:self.submitColor("orange"), btncolor="orange")
        self.createButton(color_frame, "", click_action = lambda:self.submitColor("red"), btncolor="red")
        self.createButton(color_frame, "", click_action = lambda:self.submitColor("purple"), btncolor="purple")
        self.createButton(color_frame, "", click_action = lambda:self.submitColor("blue"), btncolor="blue")
        self.createButton(color_frame, "", click_action = lambda:self.submitColor("green"), btncolor="green")

        #Export menu
        export_frame = Frame(window)
        self.createExportButton(btn_frame, "New code", self.startTest)
        self.createExportButton(btn_frame, "size-succes", self.showResults)
        self.createExportButton(btn_frame, "showtime-succes", click_action = lambda:self.__experiment.ScatterData(dataX='codeLength', dataY='percentRight'))

        btn_frame.pack(side=TOP, fill=X)
        self.__canvas.pack()
        color_frame.pack()
        export_frame.pack(side=RIGHT)

    def createLabel(self, parent, lbl_text):
        #Responsibility: Make a label and pack it
        lbl = Label(parent)
        lbl.config(text=lbl_text, font="CourierNew 20 bold")
        lbl.pack(side='left')

    def createButton(self, parent, btn_text, click_action, btncolor=None):
        #Responsibility: Make a button and pack it
        if btncolor == None:
            btn = Button(parent, command=click_action)
            btn.config(text=btn_text, font="CourierNew 20 bold")
            btn.pack(side='left')
        else:
            btn = Button(parent, command=click_action)
            btn.config(text=btn_text, font="CourierNew 20 bold", width=3,  bg=btncolor)
            btn.pack(side='left')

    def createExportButton(self, parent, btn_text, click_action):
        #Responsibility: Make a button and pack it
        btn = Button(parent, command=click_action)
        btn.config(text=btn_text, font="CourierNew 20 bold")
        btn.pack(side='bottom')

    def getScreen(self):
        #Responsibility: Pass on the writable screen to another function
        return self.__canvas

    def startTest(self):
        #Responsibility: Start a new measurement
        print("Starting test")
        self.__experiment.startMeasurement()

    def showResults(self):
        #Responsibility: ask experiment to show it's succes percentages
        self.__experiment.displayPercentage()
        self.__experiment.ScatterData(dataX='codeLength', dataY='percentRight')

    def showTimeResults(self):
        #Responsibility: scatterplot the results
        self.__experiment.ScatterData(dataX='showTime', dataY='percentRight')

    def submitColor(self, color):
        #Responsibility: Check if it's time to guess, and if so, append yellow to the color guesses
        #REFACTOR: This replaced all six loose functions that couldn't parameter previously
        if self.__guessing:
            self.__result.append(color)
            self.submitColorCode()


    def submitColorCode(self):
    #Responsibility: Print info on the submitted color and check if it's the last color to be submitted
    #if it's the last, append the code and the time it took to guess to the measurement
        print("code is now ", self.__result)
        print("Current result length: ", len(self.__result))
        if self.__experiment.getPreviousMeasurement():
            print("Last measurement length: ", self.__experiment.getPreviousMeasurement().getLength())
        if self.__experiment:
            print("experiment exists")
        if self.__experiment.getCurrentMeasurement().getLength() == len(self.__result):
            self.__experiment.setGuessedCode(self.__result)
            self.__experiment.stopTime()
            self.__guessing = False
            self.__result = []

    def disableGuessing(self):
        #Responsibility: set guessing to false, thereby disabling color input
        self.__guessing = False

    def enableGuessing(self):
        #Responsibility: set guessing to false, thereby enabling color input
        self.__guessing = True
