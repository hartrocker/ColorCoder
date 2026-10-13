from tkinter import *
#from ColorCode import colorCode
from Stopwatch import stopwatch
from Measurement import measurement
from Experiment import experiment

class board(Canvas):
    #Responsibility: Set a field for balls to move on, and set the balls in motion when controls are pressed to do so
    #Also, keep track of the statusMoving: are the balls in a continuous state of motion
    def __init__(self, root):
        window = root
        window.title("Color guessing game!")

        btn_frame = Frame(window)  # for layouting row of draw buttons
        self.create_label(btn_frame, "Menu ")
        self.create_button(btn_frame, "Start", self.startTest)
        self.create_button(btn_frame, "Stop", self.stopTest)
        self.create_button(btn_frame, "Results", self.showResults)
        self.create_button(btn_frame, "Export", self.exportResults)
        self.lengthMsg = Label(window, text='max color code length', justify=LEFT)
        self.__codeLengthInput = Entry(window, justify=LEFT)
        self.__canvas = Canvas(window, width=600, height=300, background="lightyellow")


        self.__experiment = experiment()

        color_frame = Frame(window)
        self.create_button(color_frame, "", click_action=self.submitColor("yellow"), btncolor="yellow")
        self.create_button(color_frame, "", click_action=self.submitColor("orange"), btncolor="orange")
        self.create_button(color_frame, "", click_action=self.submitColor("red"), btncolor="red")
        self.create_button(color_frame, "", click_action=self.submitColor("purple"), btncolor="purple")
        self.create_button(color_frame, "", click_action=self.submitColor("blue"), btncolor="blue")
        self.create_button(color_frame, "", click_action=self.submitColor("green"), btncolor="green")
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

    def startTest(self):
        if self.__experiment.getExperimentLength() < 1:
            length=1
            Time=5
        else:
            lastMeasurement = self.__experiment.getLastMeasurement()
            length = lastMeasurement.get()
            time = lastMeasurement.getTime()
        colorCode = thisround.getAskedCode()
        for color in colorCode:
            code = self.__canvas.create_rectangle(fill=color)
        for
        self.__canvas.after(x, self.pack)



    def stopTest(self):
        print("Stopping test")

    def showResults(self):
        print("Showing results")

    def exportResults(self):
        print("Exporting results")

    def submitColor(self, submitColor):
        print("Submitting color")

    def getLastMeasurement(self):
        length = self.__experiment.getExperimentLength()
        self.__experiment.getMeasurement(length-1)