from pages.BasePage import SearchHelper


def test_search(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    lst = main_page.check_device_id(1)
    print(lst)
    # assert "Issues" in elements
