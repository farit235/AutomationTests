from selenium.webdriver.common.by import By

# норм тема
class BasePageLocators:
    """Constant locators for elements on Base page"""
    NEW_DEVICE_ITEM_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
    INPUT_DEVICE_NAME_FIELD = (By.XPATH, "//textarea[@id='device-upsert-modal__device-name-field']")
    INPUT_DEVICE_ID_FIELD = (By.XPATH, "//textarea[@id='device-upsert-modal__device-id-field']")
    SUBMIT_NEW_DEVICE_BUTTON = (By.XPATH, "//button[@type='button'][contains(.,'Submit')]")
    TABLE_SECOND_COLUMN = (By.XPATH, "//td[2]")
    CHECKBOX_REGISTER_DEVICE = (By.XPATH, "//div[@class='custom-control custom-checkbox']/input[@name='registered']")


# class BasePageLocators:
#     """Constant locators for elements on Base page"""
#     NEW_DEVICE_ITEM_BUTTON = (By.XPATH, "//button[text()='New device']")
#     INPUT_DEVICE_NAME_FIELD = (By.XPATH, "//textarea[@id='device-upsert-modal__device-name-field']")
#     INPUT_DEVICE_ID_FIELD = (By.XPATH, "//textarea[@id='device-upsert-modal__device-id-field']")
#     SUBMIT_NEW_DEVICE_BUTTON = (By.XPATH, "//button[@type='button'][contains(.,'Submit')]")
#     TABLE_SECOND_COLUMN = (By.XPATH, "//td[2]")
#     CHECKBOX_REGISTER_DEVICE = (By.XPATH, "//*[@name='registered']")

# class BasePageLocators:
#     """Constant locators for elements on Base page"""
#     NEW_DEVICE_ITEM_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
#     INPUT_DEVICE_NAME_FIELD = (By.XPATH, "//textarea[@id='device-upsert-modal__device-name-field']")
#     INPUT_DEVICE_ID_FIELD = (By.XPATH, "//textarea[@id='device-upsert-modal__device-id-field']")
#     SUBMIT_NEW_DEVICE_BUTTON = (By.XPATH, "//button[@type='button'][contains(.,'Submit')]")
#     TABLE_SECOND_COLUMN = (By.XPATH, "//td[2]")
#     CHECKBOX_REGISTER_DEVICE = (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/form/div[1]/input")
