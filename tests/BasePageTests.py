import time
from pages.MainPage import MainPage


class TestBasePage:

    def test_search(self, browser):
        name = "name_20"
        device_id = "20"
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.click_on_add_device_button()
        main_page.enter_device_name(name)
        main_page.enter_device_id(device_id)
        main_page.click_on_submit_button()
        main_page.refresh_page()
        time.sleep(1)
        lst = main_page.check_device_id()
        assert device_id in lst

    def test_delete(self, browser):
        device_id = "20"
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.click_on_edit_device_button(device_id)
        main_page.checkout_unregistered()
        main_page.click_on_submit_button()
        main_page.click_delete_button(device_id)
        lst = main_page.check_device_id()
        assert device_id not in lst
