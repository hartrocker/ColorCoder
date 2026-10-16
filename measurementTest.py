import pytest
from Measurement import measurement
from ColorCode import colorCode

def testGetExampleCode():
    #Responsibility: Test if getExampleCode returns the color code that was set as example code
    testMeasurement = measurement(length=3)
    exampleCode = colorCode(colorlist=["blue", "red", "green"])
    testMeasurement.setAskedCode(exampleCode)
    assert testMeasurement.getExampleCode() == ["blue", "red", "green"]

def testGetGuessedCode(capsys):
    #Responsibility: Test if getGuessedCode returns the color code that was set as guessed code
    testMeasurement = measurement(length=3)
    exampleCode = colorCode(colorlist=["blue", "red", "green"])
    guessedCode = colorCode(colorlist=["blue", "red", "green"])
    testMeasurement.setAskedCode(exampleCode)
    testMeasurement.setGuessedCode(guessedCode)
    capsys.readouterr()
    assert testMeasurement.getGuessedCode() == ["blue", "red", "green"]

def testGetTimeShowed():
    #Responsibility: Test if getTimeShowed returns the time that was given when creating the measurement
    testMeasurement = measurement(time=2.5, length=2)
    assert testMeasurement.getTimeShowed() == 2.5

def testGetTimeGuessed():
    #Responsibility: Test if getTimeGuessed returns the stored response time
    testMeasurement = measurement(length=2)
    testMeasurement.setTimeResponse(4.25)
    assert testMeasurement.getTimeGuessed() == 4.25

def testGetNrGoodPositions(capsys):
    #Responsibility: Test if getNrGoodpositions returns the number of correctly guessed positions
    testMeasurement = measurement(length=3)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green"]))
    testMeasurement.setGuessedCode(colorCode(colorlist=["blue", "yellow", "green"]))
    capsys.readouterr()
    assert testMeasurement.getNrGoodpositions() == 2

def testGetNrBadPositions(capsys):
    #Responsibility: Test if getNrBadPositions returns the number of incorrectly guessed positions
    testMeasurement = measurement(length=3)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green"]))
    testMeasurement.setGuessedCode(colorCode(colorlist=["blue", "yellow", "purple"]))
    capsys.readouterr()
    assert testMeasurement.getNrBadPositions() == 2

def testGetLength():
    #Responsibility: Test if getLength returns the length of the example code
    testMeasurement = measurement(length=4)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green", "yellow"]))
    assert testMeasurement.getLength() == 4

def testGetResultTrue(capsys):
    #Responsibility: Test if getResult returns true when all positions are guessed correctly
    testMeasurement = measurement(length=3)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green"]))
    testMeasurement.setGuessedCode(colorCode(colorlist=["blue", "red", "green"]))
    capsys.readouterr()
    assert testMeasurement.getResult() == True

def testGetResultFalse(capsys):
    #Responsibility: Test if getResult returns false when a position is guessed incorrectly
    testMeasurement = measurement(length=3)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green"]))
    testMeasurement.setGuessedCode(colorCode(colorlist=["blue", "yellow", "green"]))
    capsys.readouterr()
    assert testMeasurement.getResult() == False

def testGetPercentageRight(capsys):
    #Responsibility: Test if getPercentageRight returns the percentage of correctly guessed positions
    testMeasurement = measurement(length=4)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green", "yellow"]))
    testMeasurement.setGuessedCode(colorCode(colorlist=["blue", "purple", "green", "orange"]))
    capsys.readouterr()
    assert testMeasurement.getPercentageRight() == pytest.approx(50.0)

def testSetTimeShowed():
    #Responsibility: Test if setTimeShowed stores a new show time
    testMeasurement = measurement(time=1.0, length=2)
    testMeasurement.setTimeShowed(3.5)
    assert testMeasurement.getTimeShowed() == 3.5

def testSetTimeResponse():
    #Responsibility: Test if setTimeResponse stores a new response time
    testMeasurement = measurement(length=2)
    testMeasurement.setTimeResponse(6.75)
    assert testMeasurement.getTimeGuessed() == 6.75

def testSetAskedCode():
    #Responsibility: Test if setAskedCode replaces the example code
    testMeasurement = measurement(length=2)
    exampleCode = colorCode(colorlist=["orange", "purple"])
    testMeasurement.setAskedCode(exampleCode)
    assert testMeasurement.getExampleCode() == ["orange", "purple"]

def testSetGuessedCode(capsys):
    #Responsibility: Test if setGuessedCode stores the guessed code
    testMeasurement = measurement(length=2)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red"]))
    guessedCode = colorCode(colorlist=["blue", "green"])
    testMeasurement.setGuessedCode(guessedCode)
    capsys.readouterr()
    assert testMeasurement.getGuessedCode() == ["blue", "green"]

def testSetGoodBad(capsys):
    #Responsibility: Test if setGoodBad correctly separates good and bad positions
    testMeasurement = measurement(length=4)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green", "yellow"]))
    testMeasurement.setGuessedCode(colorCode(colorlist=["blue", "purple", "green", "orange"]))
    capsys.readouterr()
    assert testMeasurement.getNrGoodpositions() == 2
    assert testMeasurement.getNrBadPositions() == 2

def testShowMeasurement(capsys):
    #Responsibility: Test if showMeasurement prints the processed measurement information
    testMeasurement = measurement(time=2.0, length=2)
    testMeasurement.setTimeResponse(3.0)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red"]))
    testMeasurement.setGuessedCode(colorCode(colorlist=["blue", "green"]))
    capsys.readouterr()
    testMeasurement.showMeasurement()
    output = capsys.readouterr().out
    assert "everything processed" in output
    assert "example code:" in output
    assert "guessed code:" in output
    assert "good positions:" in output
    assert "bad positions:" in output
    assert "showtime:" in output
    assert "guesstime:" in output

def testValidateMeasurementValid():
    #Responsibility: Test if validateMeasurement returns true when the measurement contains valid values
    testMeasurement = measurement(time=2.0, length=3)
    testMeasurement.setTimeResponse(3.0)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green"]))
    testMeasurement.setGuessedCode(colorCode(colorlist=["blue", "yellow", "green"]))
    assert testMeasurement.validateMeasurement() == True

def testValidateMeasurementInvalidTime(capsys):
    #Responsibility: Test if validateMeasurement returns false when a time is not valid
    testMeasurement = measurement(time=0, length=3)
    testMeasurement.setTimeResponse(3.0)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green"]))
    testMeasurement.setGuessedCode(colorCode(colorlist=["blue", "yellow", "green"]))
    capsys.readouterr()
    assert testMeasurement.validateMeasurement() == False

def testValidateMeasurementInvalidCode(capsys):
    #Responsibility: Test if validateMeasurement returns false when a code is not a colorCode
    testMeasurement = measurement(time=2.0, length=3)
    testMeasurement.setTimeResponse(3.0)
    testMeasurement._measurement__guessedCode = ["blue", "red", "green"]
    assert testMeasurement.validateMeasurement() == False

def testValidateMeasurementNotEnoughPositions(capsys):
    #Responsibility: Test if validateMeasurement returns false when not all positions have been processed
    testMeasurement = measurement(time=2.0, length=3)
    testMeasurement.setTimeResponse(3.0)
    testMeasurement.setAskedCode(colorCode(colorlist=["blue", "red", "green"]))
    testMeasurement._measurement__guessedCode = colorCode(colorlist=["blue", "red", "green"])
    assert testMeasurement.validateMeasurement() == False

if __name__ == '__main__':
    import pytest
    pytest.main(['measurementTest.py', '--cov=Measurement', '--cov-report=term-missing'])