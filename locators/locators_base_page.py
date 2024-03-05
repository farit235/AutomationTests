from selenium.webdriver.common.by import By


class BasePageLocators:
    """Constant locators for elements on Base page"""
    NEW_DEVICE_ITEM_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
    INPUT_DEVICE_NAME_FIELD = (By.XPATH, "//textarea[@id='device-upsert-modal__device-name-field']")
    INPUT_DEVICE_ID_FIELD = (By.XPATH, "//textarea[@id='device-upsert-modal__device-id-field']")
    SUBMIT_NEW_DEVICE_BUTTON = (By.XPATH, "//button[@type='button'][contains(.,'Submit')]")
    TABLE_SECOND_COLUMN = (By.XPATH, "//td[2]")
    CHECKBOX_REGISTER_DEVICE = (By.XPATH, "//div[@class='custom-control custom-checkbox']/input[@name='registered']")
