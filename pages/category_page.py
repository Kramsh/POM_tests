from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.category_locators import CategoryPageLocators


class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'http://testshop.qa-practice.com/shop/category/'

    def open_category(self, category_slug):
        url = f"{self.base_url}{category_slug}"
        self.open(url)
        self.wait_for_page_ready()

    def open_desks_category(self):
        self.open_category('desks-1')

    def click_steel_checkbox(self):
        self.click(CategoryPageLocators.STEEL_CHECKBOX)

    def is_product_visible(self):
        return self.is_visible(CategoryPageLocators.PRODUCT_LINK)

    def hover_over_product(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def hover_over_customizable_desk(self):
        self.hover_over_product(CategoryPageLocators.CUSTOMIZABLE_DESK_IMAGE)

    def click_shopping_cart_button(self):
        self.click(CategoryPageLocators.SHOPPING_CART_BUTTON)

    def click_proceed_to_checkout(self):
        proceed_btn = self.wait.until(
            EC.presence_of_element_located(CategoryPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(proceed_btn).pause(1).click(proceed_btn).perform()

    def get_added_product_name(self):
        return self.get_text(CategoryPageLocators.ADDED_PRODUCT_NAME)

    def add_product_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(CategoryPageLocators.SHOPPING_CART_BUTTON)
        )
        button.click()

    def open_sort_dropdown(self):
        self.click(CategoryPageLocators.SORT_DROPDOWN_BUTTON)

    def select_sort_by_name(self):
        self.click(CategoryPageLocators.SORT_BY_NAME_OPTION)

    def sort_products_by_name(self):
        self.open_sort_dropdown()
        self.select_sort_by_name()

    def get_first_product_name(self):
        first_product = self.find_element(CategoryPageLocators.FIRST_PRODUCT)
        name_element = first_product.find_element(*CategoryPageLocators.FIRST_PRODUCT_NAME)
        return name_element.text

    def hover_over_first_product(self):
        element = self.wait.until(
            EC.visibility_of_element_located(CategoryPageLocators.FIRST_PRODUCT_NAME)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.wait.until(
            EC.visibility_of_element_located(CategoryPageLocators.SHOPPING_CART_BUTTON)
        )

    def add_first_product_to_cart(self):
        self._first_product_name = self.get_first_product_name()
        self.hover_over_first_product()
        self.click_shopping_cart_button()
        self.click_proceed_to_checkout()
        self.wait_for_cart_page_loaded()

    def get_expected_product_name(self):
        return self._first_product_name

    def wait_for_cart_page_loaded(self):
        self.wait.until(
            EC.presence_of_element_located(CategoryPageLocators.ADDED_PRODUCT_NAME)
        )

    def sort_by_name(self):
        products = self.find_elements(CategoryPageLocators.PRODUCTS)
        products_list = [product.text for product in products]
        products_list.sort()
        step = products_list[0]
        splitted = step.split('\n')
        result = splitted[0]
        return result
