import random

class colorCode:
    #Responsibility: Generate and display a color code
    __VALIDCOLORS = ['blue', 'red',  'yellow', 'green', 'orange', 'purple']
    def __init__(self, length = None, colorlist = None):
        #array for holding the canvas objects in this color code
        self.__canvasItems = []
        if not length == None:
            self.__code = []
            for i in range(length):
                self.__code.append(random.choice(colorCode.__VALIDCOLORS))
        else:
            self.__code = colorlist

    def getCode(self):
        #Responsibility: return the list of colors in this code
        return self.__code

    def getLength(self):
        #Responsibility: return the amount of objects in this list (length of the code)
        return len(self.__code)

    def draw(self, board):
        #Responsibility: Display the current color code on the canvas)
        canvas = board.getScreen()
        posx = 20
        for color in self.__code:
            item = canvas.create_rectangle(posx, 20, posx+30, 50, fill=color)
            self.__canvasItems.append(item)
            posx += 32

    def undraw(self, board):
        #Responsibility: Remove the colorcode from the canvas
        canvas = board.getScreen()
        for item in self.__canvasItems:
            canvas.delete(item)

if __name__ == '__main__':
    import pytest
    pytest.main(['colorcodeTest.py', '--cov=ColorCode', '--cov-report=term-missing'])


