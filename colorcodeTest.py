import pytest
import ColorCode
from ColorCode import colorCode


def testGetCodeWithColorList():
    #Responsibility: Test if getCode returns the color list used to create the color code
    colors = ["blue", "red", "green"]
    code = colorCode(colorlist=colors)
    assert code.getCode() == colors

def testGetLength():
    #Responsibility: Test if getLength returns the number of colors in the color code
    colors = ["blue", "red", "yellow", "green"]
    code = colorCode(colorlist=colors)
    assert code.getLength() == 4

def testCreateCodeWithLength(monkeypatch):
    #Responsibility: Test if a color code of a given length is created with valid chosen colors
    def fakeChoice(colors):
        #Responsibility: Return a fixed color instead of a random color
        return "blue"

    monkeypatch.setattr(ColorCode.random, "choice", fakeChoice)
    code = colorCode(length=3)
    assert code.getCode() == ["blue", "blue", "blue"]

def testLengthOfGeneratedCode(monkeypatch):
    #Responsibility: Test if a generated color code has the requested length
    def fakeChoice(colors):
        #Responsibility: Return a fixed color instead of a random color
        return "red"

    monkeypatch.setattr(ColorCode.random, "choice", fakeChoice)
    code = colorCode(length=5)
    assert code.getLength() == 5

def testDrawCreatesRectangles():
    #Responsibility: Test if draw creates one rectangle for each color at the correct position
    colors = ["blue", "red"]
    code = colorCode(colorlist=colors)
    calls = []

    class fakeCanvas:
        def create_rectangle(self, x1, y1, x2, y2, fill):
            #Responsibility: Save rectangle data instead of drawing on a real canvas
            calls.append((x1, y1, x2, y2, fill))
            return len(calls)

    class fakeBoard:
        def getScreen(self):
            #Responsibility: Return the fake canvas used by this test
            return fakeCanvas()

    code.draw(fakeBoard())
    assert calls == [
        (20, 20, 50, 50, "blue"),
        (52, 20, 82, 50, "red")
    ]

def testUndrawDeletesCanvasItems():
    #Responsibility: Test if undraw deletes all canvas items created by draw
    colors = ["blue", "red"]
    code = colorCode(colorlist=colors)
    deletedItems = []

    class fakeCanvas:
        #Responsibility: Create a fake canvas that can be used by this test
        #MdL: I used AI to generate this test unit, cause I had no idea how to do any tests on canvas objects from another class
        def create_rectangle(self, x1, y1, x2, y2, fill):
            #Responsibility: Return a fake canvas item for each rectangle
            return fill

        def delete(self, item):
            #Responsibility: Save which fake canvas item is deleted
            deletedItems.append(item)

    class fakeBoard:
        def __init__(self):
            #Responsibility: Create the fake canvas used by this board
            self.canvas = fakeCanvas()

        def getScreen(self):
            #Responsibility: Return the fake canvas used by this test
            return self.canvas

    board = fakeBoard()
    code.draw(board)
    code.undraw(board)
    assert deletedItems == ["blue", "red"]
