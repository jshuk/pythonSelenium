####
import pytest


def test_firstProgram():
    print("First program running using pytest")


def test_secondProgram(setup):
    print("Second program running using pytest")


@pytest.mark.smoke
def test_thirdProgram():
    print("Third program running using pytest")
