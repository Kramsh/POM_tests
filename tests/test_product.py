from pages.product_page import ProductPage


def test_add_to_cart_several_items_of_product(driver):
    product_page = ProductPage(driver)
    product_page.open_office_design_software()

    product_page.skip_if_unavailable()

    product_page.add_multiple_items_to_cart(quantity=6)
    product_page.click_cart_button()

    product_name = product_page.get_product_name_in_cart()
    quantity_in_cart = product_page.get_quantity_in_cart()

    assert quantity_in_cart == "6"
    assert product_name == "Office Design Software"


def test_redirect_to_terms_and_conditions(driver):
    product_page = ProductPage(driver)
    product_page.open_office_design_software()

    product_page.skip_if_unavailable()

    product_page.click_terms_and_conditions()

    current_url = product_page.get_current_url()
    expected_url = 'http://testshop.qa-practice.com/terms'

    assert current_url == expected_url


def test_redirect_to_pinterest(driver):
    product_page = ProductPage(driver)
    product_page.open_office_design_software()

    product_page.skip_if_unavailable()

    product_page.click_pinterest_button()
    product_page.switch_to_new_window()

    current_url = product_page.get_current_url()
    assert "pinterest.com/pin/create/button" in current_url
