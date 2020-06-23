import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\jshukla\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)

driver.find_element_by_css_selector('input.search-keyword').send_keys("berr")
time.sleep(10)
driver.find_elements_by_xpath("//button[text()='ADD TO CART']")
for e in driver.find_elements_by_xpath("//button[text()='ADD TO CART']"):
    e.click()

driver.find_element_by_css_selector('a.cart-icon').click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector('input.promoCode').send_keys('rahulshettyacademy')
# implicit wait
driver.find_element_by_css_selector('button.promoBtn').click()
wait = WebDriverWait(driver, 5)
#wait.until(expected_conditions.text_to_be_present_in_element(driver.find_element_by_css_selector('span.promoInfo'),'Code applied ..!'))
driver.get_screenshot_as_file("screen.png")
