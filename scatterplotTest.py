import pytest
import Scatterplot
from Scatterplot import scatterplot


#MdL straight up admit. This one is FULL AI. I had no idea how to test matplotlib. And I already did quite a few classes, so I just generated it
#MdL I did figure out what it does though

def testDrawPlotDefaultValues(monkeypatch):
    #Responsibility: Test if drawPlot uses the default color blue and default dot size 100
    scatterCalls = []
    def fakeScatter(x, y, color, s, label):
        #Responsibility: Save the scatter values instead of drawing a real plot
        scatterCalls.append((x, y, color, s, label))
    def fakeFunction(*args, **kwargs):
        #Responsibility: Replace matplotlib functions that are not part of this test
        return None
    monkeypatch.setattr(Scatterplot.plt, "scatter", fakeScatter)
    monkeypatch.setattr(Scatterplot.plt, "title", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "xlabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "ylabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "legend", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "show", fakeFunction)
    plot = scatterplot([1, 2], [3, 4], "x", "y", "test")
    plot.drawPlot()
    assert scatterCalls == [([1, 2], [3, 4], "blue", 100, "measurements")]

def testDrawPlotCustomColor(monkeypatch):
    #Responsibility: Test if drawPlot uses the chosen color
    usedColors = []
    def fakeScatter(x, y, color, s, label):
        #Responsibility: Save the color instead of drawing a real plot
        usedColors.append(color)
    def fakeFunction(*args, **kwargs):
        #Responsibility: Replace matplotlib functions that are not part of this test
        return None
    monkeypatch.setattr(Scatterplot.plt, "scatter", fakeScatter)
    monkeypatch.setattr(Scatterplot.plt, "title", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "xlabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "ylabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "legend", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "show", fakeFunction)
    plot = scatterplot([1], [2], "x", "y", "test", color="red")
    plot.drawPlot()
    assert usedColors == ["red"]

def testDrawPlotCustomDotSize(monkeypatch):
    #Responsibility: Test if drawPlot uses the chosen dot size
    usedSizes = []
    def fakeScatter(x, y, color, s, label):
        #Responsibility: Save the dot size instead of drawing a real plot
        usedSizes.append(s)
    def fakeFunction(*args, **kwargs):
        #Responsibility: Replace matplotlib functions that are not part of this test
        return None
    monkeypatch.setattr(Scatterplot.plt, "scatter", fakeScatter)
    monkeypatch.setattr(Scatterplot.plt, "title", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "xlabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "ylabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "legend", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "show", fakeFunction)
    plot = scatterplot([1], [2], "x", "y", "test", dotSize=50)
    plot.drawPlot()
    assert usedSizes == [50]

def testDrawPlotTitle(monkeypatch):
    #Responsibility: Test if drawPlot uses the given plot title
    usedTitles = []
    def fakeTitle(title):
        #Responsibility: Save the title instead of setting it on a real plot
        usedTitles.append(title)
    def fakeFunction(*args, **kwargs):
        #Responsibility: Replace matplotlib functions that are not part of this test
        return None
    monkeypatch.setattr(Scatterplot.plt, "scatter", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "title", fakeTitle)
    monkeypatch.setattr(Scatterplot.plt, "xlabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "ylabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "legend", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "show", fakeFunction)
    plot = scatterplot([1], [2], "x", "y", "My plot")
    plot.drawPlot()
    assert usedTitles == ["My plot"]

def testDrawPlotXAxis(monkeypatch):
    #Responsibility: Test if drawPlot uses the given x axis label
    usedLabels = []
    def fakeXLabel(label):
        #Responsibility: Save the x axis label instead of setting it on a real plot
        usedLabels.append(label)
    def fakeFunction(*args, **kwargs):
        #Responsibility: Replace matplotlib functions that are not part of this test
        return None
    monkeypatch.setattr(Scatterplot.plt, "scatter", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "title", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "xlabel", fakeXLabel)
    monkeypatch.setattr(Scatterplot.plt, "ylabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "legend", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "show", fakeFunction)
    plot = scatterplot([1], [2], "Time", "y", "test")
    plot.drawPlot()
    assert usedLabels == ["Time"]

def testDrawPlotYAxis(monkeypatch):
    #Responsibility: Test if drawPlot uses the given y axis label
    usedLabels = []
    def fakeYLabel(label):
        #Responsibility: Save the y axis label instead of setting it on a real plot
        usedLabels.append(label)
    def fakeFunction(*args, **kwargs):
        #Responsibility: Replace matplotlib functions that are not part of this test
        return None
    monkeypatch.setattr(Scatterplot.plt, "scatter", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "title", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "xlabel", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "ylabel", fakeYLabel)
    monkeypatch.setattr(Scatterplot.plt, "legend", fakeFunction)
    monkeypatch.setattr(Scatterplot.plt, "show", fakeFunction)
    plot = scatterplot([1], [2], "x", "Distance", "test")
    plot.drawPlot()
    assert usedLabels == ["Distance"]
