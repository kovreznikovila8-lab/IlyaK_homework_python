import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    wait = WebDriverWait(driver, 50)

    delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_field.clear()
    delay_field.send_keys("45")

    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()

    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()

    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()

    button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
        )
    )

    screen = driver.find_element(By.CSS_SELECTOR, ".screen")
    actual_result = screen.text
    assert actual_result == "15", (
        f"Ожидался результат '15', но получен '{actual_result}'"
    )
