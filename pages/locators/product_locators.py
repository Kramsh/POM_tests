from selenium.webdriver.common.by import By


class ProductPageLocators:

    PRODUCT_UNAVAILABLE = (By.ID, "product_unavailable")
    PRODUCT_UNAVAILABLE_TEXT = (By.XPATH, "//div[@id='product_unavailable']//h3")

    ADD_ONE_BUTTON = (
        By.XPATH, 
        "//a[@title='Add one' and contains(@class, 'js_add_cart_json')]"
    )

    ADD_ONE_BUTTON = (
        By.XPATH, 
        "//a[@title='Add one' and contains(@class, 'js_add_cart_json')]"
    )
    REMOVE_ONE_BUTTON = (
        By.XPATH,
        "//a[@title='Remove one' and contains(@class, 'js_add_cart_json')]"
    )
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input.quantity.text-center[name='add_qty']")

    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//a[@id='add_to_cart' and @role='button' and contains(@class, 'js_check_product')]"
    )

    CART_QUANTITY_BADGE = (By.CSS_SELECTOR, "sup.my_cart_quantity.badge")
    CART_BUTTON = (
        By.XPATH,
        "//a[@aria-label='eCommerce cart' and contains(@class, 'o_navlink_background')]"
    )

    PRODUCT_NAME_IN_CART = (
        By.XPATH,
        "//h6[@class='d-inline align-top h6 fw-bold' and normalize-space()='Office Design Software']"
    )
    QUANTITY_IN_CART = (
        By.CSS_SELECTOR,
        "div[name='website_sale_cart_line_quantity'] input.js_quantity"
    )

    TERMS_LINK = (By.LINK_TEXT, "Terms and Conditions")

    PINTEREST_BUTTON = (By.CSS_SELECTOR, ".s_share_pinterest")
