####
import pytest


def test_firstProgram1():
    print("First program running using pytest")


#@pytest.mark.smoke
def test_secondProgram1():
    print("Second program1 running using pytest")


def test_methodRun(setup):
    print(" I am the method run")

def test_cross(crossBrowser):
    print(crossBrowser)




