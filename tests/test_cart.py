from pages.cart_page import CartPage


def test_cart_is_empty_by_default(driver):
    cart_page = CartPage(driver)
    cart_page.open_cart()

    assert cart_page.is_cart_empty()


def test_search_in_cart(driver):
    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.search_product("Corner Desk Left Sit")
    cart_page.click_first_search_result()
    expected_url = 'http://testshop.qa-practice.com/shop/furn-1118-corner-desk-left-sit-18'
    actual_url = cart_page.get_current_url()

    assert actual_url == expected_url


def test_check_items_in_categories_dropdown_in_cart(driver):
    cart_page = CartPage(driver)
    cart_page.open_cart()

    menu_count = cart_page.get_dropdown_menu_count()
    assert menu_count == 2

    menu_texts = cart_page.get_dropdown_menu_texts()
    expected_texts = ["Desks", "Furnitures"]
    assert menu_texts == expected_texts
