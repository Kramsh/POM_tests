from pages.category_page import CategoryPage


def test_choose_steel_checkbox(driver):
    category_page = CategoryPage(driver)
    category_page.open_desks_category()
    category_page.click_steel_checkbox()

    assert category_page.is_product_visible()


def test_add_to_cart(driver):
    category_page = CategoryPage(driver)
    category_page.open_desks_category()
    category_page.add_first_product_to_cart()

    expected_name = category_page.get_expected_product_name()
    actual_name = category_page.get_added_product_name()

    assert expected_name in actual_name


def test_sort_by_name(driver):
    category_page = CategoryPage(driver)
    category_page.open_desks_category()
    category_page.sort_products_by_name()

    first_product_name = category_page.get_first_product_name()
    expected_name = "Acoustic Bloc Screens"

    assert first_product_name == expected_name
