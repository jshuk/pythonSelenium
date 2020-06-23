import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestExample(BaseClass):

    def test_Demo1(self):
        log = self.test_getLogger()
        log.info("This is Debug")
        log.warning("This is warning")
        print("Demo1")


    def test_Demo2(self):
        print("Demo2")

    def test_Demo3(self):
        print("Demo3")
