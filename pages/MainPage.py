from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from locators.locators_base_page import BasePageLocators as Locators


class MainPage(BasePage):

    def click_on_edit_device_button(self, device_id: str):
        """Find exactly edit device button function"""
        rows = self.find_elements(Locators.TABLE_SECOND_COLUMN)
        counter = 1
        for row in rows:
            if str(device_id) == row.text:
                break
            counter += 1
        locator = f"//tr[{counter}]/td[11]/button"
        LOCATOR_EDIT_DEVICE_BUTTON = (By.XPATH, locator)
        edit_button = self.find_element(LOCATOR_EDIT_DEVICE_BUTTON)
        edit_button.click()

    def click_delete_button(self, device_id: str):
        """Delete row by button function"""
        rows = self.find_elements(Locators.TABLE_SECOND_COLUMN)
        counter = 1
        for row in rows:
            if str(device_id) == row.text:
                break
            counter += 1
        locator = f"//tr[{counter}]/td[13]/button"
        LOCATOR_DELETE_DEVICE_BUTTON = (By.XPATH, locator)
        delete_button = self.find_element(LOCATOR_DELETE_DEVICE_BUTTON)
        delete_button.click()

    def checkout_unregistered(self):
        """Checkbox unregistered"""
        checkbox = self.find_element(Locators.CHECKBOX_REGISTER_DEVICE)
        checkbox.click()

    def check_device_id(self):
        """Check device id function in table"""
        device_id_list = []
        device_id_list_links = self.find_elements(Locators.TABLE_SECOND_COLUMN)
        for item in device_id_list_links:
            device_id_list.append(item.text)
        return device_id_list

    def click_on_add_device_button(self):
        """Click add device button function"""
        a = self.find_element(Locators.NEW_DEVICE_ITEM_BUTTON)
        a.click()

    def enter_device_name(self, name: str):
        """Input device name function"""
        input_field = self.find_element(Locators.INPUT_DEVICE_NAME_FIELD)
        input_field.send_keys(name)
        return input_field

    def enter_device_id(self, device_id: str):
        """Input device id function"""
        input_field = self.find_element(Locators.INPUT_DEVICE_ID_FIELD)
        input_field.send_keys(device_id)
        return input_field

    def click_on_submit_button(self):
        """Click submit button function"""
        submit_button = self.find_element(Locators.SUBMIT_NEW_DEVICE_BUTTON)
        # click that way, because checkbox is overlapped by label next to it
        self.driver.execute_script("arguments[0].click();", submit_button)
