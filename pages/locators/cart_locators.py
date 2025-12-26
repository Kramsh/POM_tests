from selenium.webdriver.common.by import By


class CartPageLocators:
    EMPTY_CART_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-info')]")
    SEARCH_BUTTON = (By.XPATH, "//a[contains(@class, 'btn rounded-circle')]")
    SEARCH_INPUT = (By.XPATH, "//div[@id='o_search_modal']//input[@placeholder='Search...']")
    SEARCH_RESULT_ITEM = (By.XPATH, "//div[contains(@class, 'o_search_result_item')]")
    CATEGORIES_DROPDOWN = (By.ID, "top_menu")
    DROPDOWN_MENU_ITEMS = (By.CSS_SELECTOR, "ul.dropdown-menu.show li a")