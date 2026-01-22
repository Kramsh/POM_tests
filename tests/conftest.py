import pytest
from selenium import webdriver
import random


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.save_screenshot(f'screen{random.randrange(1, 100000)}.png')
    driver.quit()
