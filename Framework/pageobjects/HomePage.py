from selenium.webdriver.common.by import By

from Framework.common.Baseclass import BaseClass


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    #cretae tuple
    search = (By.CSS_SELECTOR, "input.search-keyword")
    addToCart = (By.XPATH, "//button[text()='ADD TO CART']")
    cartIcon = (By.CSS_SELECTOR, "a.cart-icon")
    proceedCheckout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    selectID = (By.ID, "exampleFormControlSelect1")

    def searchBox(self):
        return self.driver.find_element(*HomePage.search)

    def addToCartItems(self):
        return self.driver.find_elements(*HomePage.addToCart)

    def getcartIcon(self):
        return self.driver.find_element(*HomePage.cartIcon)

    def getProceedCheckout(self):
        return self.driver.find_element(*HomePage.proceedCheckout)

    def getSelectID(self):
        return self.driver.find_element(*HomePage.selectID)