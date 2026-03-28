import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


class TestSlowCalculator:

    @pytest.fixture
    def driver(self):
        chrome_options = Options()
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_addition_with_delay(self, driver) -> None:
        calc_page = CalculatorPage(driver)

        calc_page.open()
        calc_page.set_delay(45)

        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

        result = calc_page.get_result()

        assert result == "15", f"Expected '15', but got '{result}'"
