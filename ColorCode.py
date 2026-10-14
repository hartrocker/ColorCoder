import tkinter
import random



class colorCode:
    #Responsibility: Generate and display a color code
    __VALIDCOLORS = ['blue', 'red',  'yellow', 'green', 'orange', 'purple']
    def __init__(self, length = None, colorlist = None):
        self.__item = []
        if not length == None:
            #self.__canvas = canvas
            self.__code = []
            for i in range(length):
                self.__code.append(random.choice(colorCode.__VALIDCOLORS))
        else:
            self.__code = colorlist

    '''
    def getCanvas(self):
        return self.__canvas
    '''

    def getCode(self):
        #Responsibility: return the list of colors in this code
        return self.__code

    def getLength(self):
        #Responsibility: return the amount of objects in this list (length of the code)
        return len(self.__code)

    def draw(self, canvas):
        #Responsibility: Display the current color code on the canvas)
        self.__canvas = canvas
        posx = 20
        for color in self.__code:
            item = canvas.create_rectangle(posx, 20, posx+30, 50, fill=color)
            self.__item.append(item)
            posx += 32

    def undraw(self):
        #Responsibility: Remove the colorcode from the canvas
        for item in self.__item:
            self.__canvas.delete(item)

    '''
    def setCode(self, colors):
        validCode = True
        for color in colors:
            if color not in colorCode.__VALIDCOLORS:
                validCode = False
        if validCode:
            self.__code = colorCode.__VALIDCOLORS
        else:
            return
    '''

