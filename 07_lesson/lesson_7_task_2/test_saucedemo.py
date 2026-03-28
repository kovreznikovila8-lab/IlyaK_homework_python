import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Класс страницы авторизации"""

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

        # Локаторы элементов
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        """Открыть страницу авторизации"""
        self.driver.get(self.url)

    def enter_username(self, username):
        """Ввести имя пользователя"""
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        """Ввести пароль"""
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        )
        password_field.send_keys(password)

    def click_login_button(self):
        """Нажать кнопку входа"""
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_btn.click()


class InventoryPage:
    """Класс главной страницы магазина (инвентаря)"""

    def __init__(self, driver):
        self.driver = driver

        # Локаторы элементов
        self.add_to_cart_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_to_cart_bolt_tshirt = (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        self.add_to_cart_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        """Добавить рюкзак в корзину"""
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_backpack)
        )
        add_button.click()

    def add_bolt_tshirt_to_cart(self):
        """Добавить футболку в корзину"""
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_bolt_tshirt)
        )
        add_button.click()

    def add_onesie_to_cart(self):
        """Добавить комбинезон в корзину"""
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_onesie)
        )
        add_button.click()

    def go_to_cart(self):
        """Перейти в корзину"""
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.shopping_cart_link)
        )
        cart_link.click()


class CartPage:
    """Класс страницы корзины"""

    def __init__(self, driver):
        self.driver = driver

        # Локаторы элементов
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        """Нажать кнопку Checkout"""
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_btn.click()

    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        items = self.driver.find_elements(*self.cart_items)
        return len(items)


class CheckoutPage:
    """Класс страницы оформления заказа"""

    def __init__(self, driver):
        self.driver = driver

        # Локаторы элементов
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Заполнить форму оформления заказа"""
        # Заполняем имя
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name_input)
        )
        first_name_field.send_keys(first_name)

        # Заполняем фамилию
        last_name_field = self.driver.find_element(*self.last_name_input)
        last_name_field.send_keys(last_name)

        # Заполняем почтовый индекс
        postal_code_field = self.driver.find_element(*self.postal_code_input)
        postal_code_field.send_keys(postal_code)

        # Нажимаем кнопку Continue
        continue_btn = self.driver.find_element(*self.continue_button)
        continue_btn.click()

    def get_total_amount(self):
        """Получить итоговую сумму"""
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_label)
        )
        total_text = total_element.text
        # Извлекаем числовое значение из текста "Total: $XX.XX"
        total_amount = float(total_text.split("$")[1])
        return total_amount


class TestSaucedemo(unittest.TestCase):
    """Тестовый класс для проверки интернет-магазина"""

    def setUp(self):
        """Настройка теста: создание и настройка драйвера Firefox"""
        # Настройка опций Firefox
        firefox_options = Options()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")

        # Создаем драйвер Firefox
        self.driver = webdriver.Firefox(options=firefox_options)
        self.driver.maximize_window()

        # Создаем объекты страниц
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def tearDown(self):
        """Завершение теста: закрытие драйвера"""
        if self.driver:
            self.driver.quit()

    def test_checkout_total(self):
        """Тест проверки итоговой суммы в корзине"""

        # Шаг 1: Открыть сайт магазина
        self.login_page.open()

        # Шаг 2: Авторизоваться как standard_user
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login_button()

        # Шаг 3: Добавить товары в корзину
        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.add_bolt_tshirt_to_cart()
        self.inventory_page.add_onesie_to_cart()

        # Шаг 4: Перейти в корзину
        self.inventory_page.go_to_cart()

        # Проверяем, что в корзине 3 товара
        cart_items_count = self.cart_page.get_cart_items_count()
        self.assertEqual(cart_items_count, 3, "В корзине должно быть 3 товара")

        # Шаг 5: Нажать кнопку Checkout
        self.cart_page.click_checkout()

        # Шаг 6: Заполнить форму своими данными
        self.checkout_page.fill_checkout_form("Иван", "Петров", "123456")

        # Шаг 7: Прочитать итоговую стоимость
        total_amount = self.checkout_page.get_total_amount()

        # Шаг 8: Проверить, что итоговая сумма равна $58.29
        expected_total = 58.29
        self.assertEqual(
            total_amount,
            expected_total,
            f"Итоговая сумма должна быть ${expected_total}, "
            f"получено ${total_amount}"
        )


if __name__ == "__main__":
    # Запуск теста
    unittest.main(verbosity=2)
