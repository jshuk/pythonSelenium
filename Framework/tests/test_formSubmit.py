import pytest
from selenium.webdriver.support.select import Select

from Framework.common.Baseclass import BaseClass
from Framework.pageobjects.HomePage import HomePage




class TestTwo(BaseClass):

    def test_form_submit(self, dataLoad):
        log = self.test_getLogger()
        homePage = HomePage(self.driver)
        self.driver.find_element_by_name('name').send_keys(dataLoad["firstname"])
        print(self.driver.find_element_by_name('name').get_attribute('value'))
        self.driver.find_element_by_id("exampleCheck1").click()
        print(self.driver.find_element_by_id("exampleCheck1").is_selected())
        log.debug("Debug logging ")
        # drpdwons
        self.selectOptionByText(dataLoad["Gender"], homePage.getSelectID())
  ###nfnfnfnnf
        self.driver.find_element_by_css_selector('input.btn-success').click()
        msg = self.driver.find_element_by_css_selector('div.alert-success').text
        assert 'Success22! The Form has been submitted successfully!.' in msg
        self.driver.get_screenshot_as_file("screen1.png")
        log.info("Refreshing the browser")
        self.driver.refresh()

    # @pytest.fixture(params=[("Rahul","Shetty","Male"),("Jaya","Shukla","Female")])
    @pytest.fixture(params=[{'firstname': 'Rahul', 'Gender': 'Female'}, {'firstname': 'Anshika', 'Gender': 'Female'}])
    def dataLoad(self, request):
        return request.param
