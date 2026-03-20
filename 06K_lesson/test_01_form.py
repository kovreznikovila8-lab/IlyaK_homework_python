import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_form_submit_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, 10)

    first_name_field = driver.find_element(By.NAME, "first-name")
    first_name_field.send_keys("Иван")

    last_name_field = driver.find_element(By.NAME, "last-name")
    last_name_field.send_keys("Петров")

    address_field = driver.find_element(By.NAME, "address")
    address_field.send_keys("Ленина, 55-3")

    email_field = driver.find_element(By.NAME, "e-mail")
    email_field.send_keys("test@skypro.com")

    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.send_keys("+7985899998787")

    city_field = driver.find_element(By.NAME, "city")
    city_field.send_keys("Москва")

    country_field = driver.find_element(By.NAME, "country")
    country_field.send_keys("Россия")

    job_field = driver.find_element(By.NAME, "job-position")
    job_field.send_keys("QA")

    company_field = driver.find_element(By.NAME, "company")
    company_field.send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    submit_button.click()

    try:
        zip_code_div = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".alert-danger .zip-code")
            )
        )
        assert "alert-danger" in zip_code_div.get_attribute("class")
    except TimeoutException:
        zip_field_parent = driver.find_element(By.CSS_SELECTOR, ".zip-code")
        assert "alert-danger" in zip_field_parent.get_attribute("class")

    fields_to_check = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for field_name in fields_to_check:
        try:
            field_element = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, f".alert-success .{field_name}")
                )
            )
            assert "alert-success" in field_element.get_attribute("class")
        except TimeoutException:
            field_parent = driver.find_element(
                By.CSS_SELECTOR, f".{field_name}"
            )
            assert "alert-success" in field_parent.get_attribute("class")

    zip_field_parent = driver.find_element(By.CSS_SELECTOR, ".zip-code")
    assert "alert-success" not in zip_field_parent.get_attribute("class")
