import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Framework.tests.conftest import setup


# using fixture for browser invocation
@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyPresence(self,text):
        element = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(By.XPATH,text))

    def selectOptionByText(self,text,locator):
        drpdown = Select(locator)
        drpdown.select_by_visible_text(text)





    def test_getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('logfile1.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s :%(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(filehandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger