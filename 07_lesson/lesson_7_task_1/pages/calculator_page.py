from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    # Locators
    DELAY_INPUT = (By.ID, "delay")
    RESULT_DISPLAY = (By.CLASS_NAME, "screen")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        base_url = "https://bonigarcia.dev"
        path = "/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(base_url + path)

    def set_delay(self, seconds: int) -> None:
        delay_field = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text: str) -> None:
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def get_result(self) -> str:
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_DISPLAY)
        )
        return result_element.text
