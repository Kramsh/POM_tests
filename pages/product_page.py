import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.product_locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'http://testshop.qa-practice.com/shop/'

    def is_product_available(self):
        return self.is_element_hidden(ProductPageLocators.PRODUCT_UNAVAILABLE)

    def skip_if_unavailable(self):
        if not self.is_product_available():
            message = "Product is not available for sale"
            try:
                unavailable_text = self.get_text(ProductPageLocators.PRODUCT_UNAVAILABLE_TEXT)
                message = f"Product unavailable: {unavailable_text}"
            except:
                pass
            pytest.skip(message)

    def open_product(self, product_slug):
        url = f"{self.base_url}{product_slug}"
        self.open(url)
        self.wait_for_page_ready()

    def open_office_design_software(self):
        self.open_product('furn-9999-office-design-software-7?category=9')

    def click_add_one(self, times=1):
        for _ in range(times):
            self.click(ProductPageLocators.ADD_ONE_BUTTON)

    def click_add_to_cart(self):
        self.click(ProductPageLocators.ADD_TO_CART_BUTTON)

    def wait_for_cart_badge_quantity(self, expected_quantity):
        self.wait.until(
            EC.text_to_be_present_in_element(
                ProductPageLocators.CART_QUANTITY_BADGE,
                str(expected_quantity)
            )
        )

    def click_cart_button(self):
        self.click(ProductPageLocators.CART_BUTTON)

    def get_product_name_in_cart(self):
        return self.get_text(ProductPageLocators.PRODUCT_NAME_IN_CART)

    def get_quantity_in_cart(self):
        element = self.wait.until(
            EC.visibility_of_element_located(ProductPageLocators.QUANTITY_IN_CART)
        )
        return element.get_attribute("value")

    def add_multiple_items_to_cart(self, quantity):
        self.click_add_one(times=quantity - 1)

        self.click_add_to_cart()

        self.wait_for_cart_badge_quantity(quantity)

    def click_terms_and_conditions(self):
        self.click(ProductPageLocators.TERMS_LINK)

    def click_pinterest_button(self):
        self.click(ProductPageLocators.PINTEREST_BUTTON)

    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))

        original_window = self.driver.current_window_handle

        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

        return original_window
