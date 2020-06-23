import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Framework.common.Baseclass import BaseClass
from Framework.pageobjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        hp = HomePage(self.driver)
        hp.searchBox().send_keys("berr")
        time.sleep(10)
        ##
        items = hp.addToCartItems()
        for e in items:
            e.click()
         ##
        hp.getcartIcon().click()
        hp.getProceedCheckout().click()
        self.driver.find_element_by_css_selector('input.promoCode').send_keys('rahulshettyacademy')
        # implicit wait
        self.driver.find_element_by_css_selector('button.promoBtn').click()
        wait = WebDriverWait(self.driver, 5)
        self.driver.get_screenshot_as_file("screen.png")


