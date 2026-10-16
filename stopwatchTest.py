#MdL took me some fidgetting to get the coverage test going in a seperate file
#MdL I just try to use it as basic as I can, pytest -- verbose stopwatchTest.py --cov=Stopwatch

import pytest
import pytest_cov
import Stopwatch
from Stopwatch import stopwatch


def testGetStartTime(monkeypatch):
    #Responsibility: Test if stopTimer saves the current time as the new stop time
    # MdL: function to return a faketime. This will replace all time.time() calls (see comments further on)
    def fakeTime():
        #Responsibility: Return a fixed time for this test
        return 10.123

    # MdL: something new I learned! Unit testing with times is rather hard, monkeypatch is a utility that helps mimicking times
    # MdL: the line below means 'replace all times in the class stopwatch with fake_time
    monkeypatch.setattr(Stopwatch.time, "time", fakeTime)
    sw = stopwatch()
    assert sw.getStartTime() == pytest.approx(10.12)

def testGetStopTime(monkeypatch):
    #Responsibility: Test if getStopTime returns the saved stop time rounded to two decimals
    def fakeTime():
        #Responsibility: Return a fixed time for this test
        return 20.456

    monkeypatch.setattr(Stopwatch.time, "time", fakeTime)
    sw = stopwatch()
    assert sw.getStopTime() == pytest.approx(20.46)

def testGetPassedTime(monkeypatch):
    #Responsibility: Test if getPassedTime returns the difference between start and stop time
    times = iter([10.0, 12.345])

    def fakeTime():
        return next(times)

    monkeypatch.setattr(Stopwatch.time, "time", fakeTime)
    sw = stopwatch()
    assert sw.getPassedTime() == pytest.approx(2.35)

def testStartTimer(monkeypatch):
    #Responsibility: Test if startTimer saves the current time as the new start time
    times = iter([10.0, 11.0, 25.678])

    def fakeTime():
        return next(times)

    monkeypatch.setattr(Stopwatch.time, "time", fakeTime)
    sw = stopwatch()
    sw.startTimer()
    assert sw.getStartTime() == pytest.approx(25.68)

def testStopTimer(monkeypatch):
    #Responsibility: Test if getStartTime returns the saved start time rounded to two decimals
    #Responsibility: Test if stopTimer saves the current time as the new stop time
    times = iter([10.0, 11.0, 30.789])

    def fakeTime():
        return next(times)

    monkeypatch.setattr(Stopwatch.time, "time", fakeTime)
    sw = stopwatch()
    sw.stopTimer()
    assert sw.getStopTime() == pytest.approx(30.79)

def testPassedTimeAfterStopTimer(monkeypatch):
    #Responsibility: Test if passed time is updated after stopping the timer
    times = iter([10.0, 11.0, 30.789])

    def fakeTime():
        return next(times)

    monkeypatch.setattr(Stopwatch.time, "time", fakeTime)
    sw = stopwatch()
    sw.stopTimer()
    assert sw.getPassedTime() == pytest.approx(20.79)
