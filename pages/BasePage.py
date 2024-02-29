from model.BaseApp import BasePage
from selenium.webdriver.common.by import By


class SearchLocators:
    LOCATOR_NEW_DEVICE_ITEM = (By.CLASS_NAME, "col-md-auto")
    LOCATOR_INPUT_DEVICE_NAME_FIELD = (By.ID, "device-upsert-modal__device-name-field")
    LOCATOR_INPUT_DEVICE_ID_FIELD = (By.ID, "device-upsert-modal__device-id-field")
    LOCATOR_SUBMIT_NEW_DEVICE = (By.CLASS_NAME, "btn btn-primary")
    LOCATOR_DEVICE_ID_COLUMN = (By.XPATH, "//selection/div/div/table/tbody/tr/td[@aria-colindex='2']")


class SearchHelper(BasePage):

    def check_device_id(self, device_id):
        """Check device id function in table"""
        device_id_list = self.find_elements(SearchLocators.LOCATOR_DEVICE_ID_COLUMN)
        return device_id_list

    def click_on_add_device_button(self):
        """Click button function"""
        return self.find_element(SearchLocators.LOCATOR_NEW_DEVICE_ITEM, time=10).click()

    def enter_device_name(self, name):
        """Input device name function"""
        input_field = self.find_element(SearchLocators.LOCATOR_INPUT_DEVICE_NAME_FIELD)
        input_field.send_keys(name)
        return input_field

    def enter_device_id(self, device_id):
        """Input device id function"""
        input_field = self.find_element(SearchLocators.LOCATOR_INPUT_DEVICE_ID_FIELD)
        input_field.send_keys(device_id)
        return input_field

    def click_on_submit_button(self):
        """Click button function"""
        return self.find_element(SearchLocators.LOCATOR_SUBMIT_NEW_DEVICE, time=10).click()
