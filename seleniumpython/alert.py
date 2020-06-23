from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\jshukla\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector('input#name').send_keys("Option3")
driver.find_element_by_css_selector('input#alertbtn').click()
#
alert1= driver.switch_to.alert
print(alert1.text)
alert1.accept()

driver.quit()