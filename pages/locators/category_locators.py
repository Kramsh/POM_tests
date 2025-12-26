from selenium.webdriver.common.by import By


class CategoryPageLocators:
    STEEL_CHECKBOX = (By.ID, "1-1")

    PRODUCT_LINK = (By.XPATH, "//a[contains(@class, 'text-decoration-none')]")
    CUSTOMIZABLE_DESK_IMAGE = (
        By.CSS_SELECTOR, 
        "a.oe_product_image_link[href='/shop/customizable-desk-9?category=1']"
    )
    FIRST_PRODUCT = (
        By.XPATH,
        "(//td[@class='oe_product']//div[contains(@class,'o_wsale_product_grid_wrapper')])[1]"
    )
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, "div.o_wsale_product_information_text h6 a")

    SHOPPING_CART_BUTTON = (
        By.XPATH,
        "//a[@role='button' and @aria-label='Shopping cart' and contains(@class,'a-submit')]"
    )

    PROCEED_TO_CHECKOUT_BUTTON = (
        By.XPATH,
        "//div[@role='dialog' and contains(@class,'show')]"
        "//button[.//span[normalize-space()='Proceed to Checkout']]"
    )
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "h6.d-inline.align-top.h6.fw-bold")

    SORT_DROPDOWN_BUTTON = (
        By.XPATH,
        "//a[@role='button' and contains(@class, 'dropdown-toggle')]"
        "[.//span[contains(normalize-space(),'Featured')]]"
    )
    SORT_BY_NAME_OPTION = (
        By.XPATH,
        "//a[@role='menuitem' and contains(@class, 'dropdown-item')]"
        "[.//span[contains(normalize-space(),'Name (A-Z)')]]"
    )
