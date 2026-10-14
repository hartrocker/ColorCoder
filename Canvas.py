from tkinter import *
from Experiment import experiment

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
        self.create_label(btn_frame, "Menu ")
        self.create_button(btn_frame, "New code", self.startTest)
        self.create_button(btn_frame, "Results", self.showResults)

        #Color input menu
        color_frame = Frame(window)
        #why can't I use a variable when calling the click_action... would make appending colors so much easier
        self.create_button(color_frame, "", click_action=self.submitYellow, btncolor="yellow")
        self.create_button(color_frame, "", click_action=self.submitOrange, btncolor="orange")
        self.create_button(color_frame, "", click_action=self.submitRed, btncolor="red")
        self.create_button(color_frame, "", click_action=self.submitPurple, btncolor="purple")
        self.create_button(color_frame, "", click_action=self.submitBlue, btncolor="blue")
        self.create_button(color_frame, "", click_action=self.submitGreen, btncolor="green")

        btn_frame.pack()
        self.__canvas.pack()
        color_frame.pack()

    def create_label(self, parent, lbl_text):
        #Responsibility: Make a label and pack it
        lbl = Label(parent)
        lbl.config(text=lbl_text, font="CourierNew 20 bold")
        lbl.pack(side='left')

    def create_button(self, parent, btn_text, click_action, btncolor=None):
        #Responsibility: Make a button and pack it
        if btncolor == None:
            btn = Button(parent, command=click_action)
            btn.config(text=btn_text, font="CourierNew 20 bold")
            btn.pack(side='left')
        else:
            btn = Button(parent, command=click_action)
            btn.config(text=btn_text, font="CourierNew 20 bold", width=3,  bg=btncolor)
            btn.pack(side='left')

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

    def exportResults(self):
        #Responsibility: scatterplot the results
        print("Exporting results")

    def submitYellow(self):
        #Responsibility: Check if it's time to guess, and if so, append yellow to the color guesses
        if self.__guessing:
            self.__result.append('yellow')
            self.submitColorCode()

    def submitOrange(self):
        #Responsibility: Check if it's time to guess, and if so, append orange to the color guesses
        if self.__guessing:
            self.__result.append('orange')
            self.submitColorCode()

    def submitRed(self):
        #Responsibility: Check if it's time to guess, and if so, append red to the color guesses
        if self.__guessing:
            self.__result.append('red')
            self.submitColorCode()

    def submitPurple(self):
        #Responsibility: Check if it's time to guess, and if so, append purple to the color guesses
        if self.__guessing:
            self.__result.append('purple')
            self.submitColorCode()

    def submitBlue(self):
        #Responsibility: Check if it's time to guess, and if so, append blue to the color guesses
        if self.__guessing:
            self.__result.append('blue')
            self.submitColorCode()

    def submitGreen(self):
        #Responsibility: Check if it's time to guess, and if so, append green to the color guesses
        if self.__guessing:
            self.__result.append('green')
            self.submitColorCode()

    def submitColorCode(self):
    #Responsibility: Print info on the submitted color and check if it's the last color to be submitted
    #if it's the last, append the code and the time it took to guess to the measurement
        print("code is now ", self.__result)
        print("Current result length: ", len(self.__result))
        print("Last measurement length: ", self.__experiment.getLastLength())
        if self.__experiment:
            print("experiment exists")
        if self.__experiment.getLastLength() == len(self.__result):
            self.__experiment.stop()
            #self.__experiment.getLastLength()
            self.__experiment.setGuessedCode(self.__result)
            self.__result = []
            self.__guessing = False

    def disableGuessing(self):
        #Responsibility: set guessing to false, thereby disabling color input
        self.__guessing = False

    def enableGuessing(self):
        #Responsibility: set guessing to false, thereby enabling color input
        self.__guessing = True

    def submitGuess(self):
        print("submitting guess")