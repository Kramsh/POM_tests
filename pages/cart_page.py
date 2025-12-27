from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.cart_locators import CartPageLocators


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'http://testshop.qa-practice.com/shop/cart'

    def open_cart(self):
        self.open(self.url)
        self.wait_for_page_ready()

    def get_empty_cart_message(self):
        return self.get_text(CartPageLocators.EMPTY_CART_MESSAGE)

    def is_cart_empty(self):
        message = self.get_empty_cart_message()
        return 'Your cart is empty!' in message

    def open_search(self):
        self.click(CartPageLocators.SEARCH_BUTTON)
        self.wait.until(EC.visibility_of_element_located(CartPageLocators.SEARCH_INPUT))

    def search_product(self, product_name):
        self.open_search()
        self.send_keys(CartPageLocators.SEARCH_INPUT, product_name)
        self.wait.until(EC.visibility_of_element_located(CartPageLocators.SEARCH_RESULT_ITEM))

    def click_first_search_result(self):
        self.click(CartPageLocators.SEARCH_RESULT_ITEM)

    def hover_categories_dropdown(self):
        element = self.find_element(CartPageLocators.CATEGORIES_DROPDOWN)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def get_dropdown_menu_items(self):
        self.hover_categories_dropdown()
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(CartPageLocators.DROPDOWN_MENU_ITEMS)
        )
        return elements

    def get_dropdown_menu_texts(self):
        items = self.get_dropdown_menu_items()
        return [item.text.strip() for item in items]

    def get_dropdown_menu_count(self):
        items = self.get_dropdown_menu_items()
        return len(items)
