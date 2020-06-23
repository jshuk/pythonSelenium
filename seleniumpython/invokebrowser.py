from selenium import webdriver

# driver object
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\jshukla\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
driver.find_element_by_name('name').send_keys("Jaya Shukla")
print(driver.find_element_by_name('name').get_attribute('value'))
driver.find_element_by_id("exampleCheck1").click()
print(driver.find_element_by_id("exampleCheck1").is_selected())

# drpdwons
drpdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
drpdown.select_by_visible_text('Female')

driver.find_element_by_css_selector('input.btn-success').click()
msg = driver.find_element_by_css_selector('div.alert-success').text
assert 'Success! The Form has been submitted successfully!.' in msg

driver.quit()
