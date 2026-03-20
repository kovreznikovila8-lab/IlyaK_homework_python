import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_saucedemo_checkout_total(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    add_backpack = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    add_backpack.click()

    add_tshirt = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
    )
    add_tshirt.click()

    add_onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    add_onesie.click()

    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    first_name_field = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name_field.send_keys("Иван")

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Петров")

    postal_code_field = driver.find_element(By.ID, "postal-code")
    postal_code_field.send_keys("123456")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text

    expected_total = "$58.29"
    assert total_text == expected_total, (
        f"Ожидалась итоговая сумма '{expected_total}', "
        f"но получена '{total_text}'"
    )
