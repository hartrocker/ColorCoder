import matplotlib.pyplot as plt
import numpy as np

class scatterplot:
    def __init__(self, x, y, xAxis, yAxis, title, color = None, dotSize = None):
        self.__Xvalues = x
        self.__Yvalues = y
        self.__xAxis = xAxis
        self.__yAxis = yAxis
        self.__title = title
        if dotSize == None:
            self.__dotSize = 100
        else:
            self.__dotSize = dotSize
        if color == None:
            self.__color = 'blue'
        else:
            self.__color = color

    def drawPlot(self):
        #plt.plot(self.__Xvalues, self.__Yvalues, self.__color)
        plt.scatter(self.__Xvalues,
                self.__Yvalues,
                color = self.__color,
                s = self.__dotSize,
                label = 'measurements' )
        plt.title(self.__title)
        plt.xlabel(self.__xAxis)
        plt.ylabel(self.__yAxis)

        plt.legend()
        plt.show()
