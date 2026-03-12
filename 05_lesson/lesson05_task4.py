from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка драйвера Firefox
driver = webdriver.Firefox()

try:
    # Открыть страницу логина
    driver.get("http://the-internet.herokuapp.com/login")
    driver.maximize_window()
    
    # Явное ожидание загрузки страницы
    wait = WebDriverWait(driver, 10)
    
    # Шаг 1: Найти поле username и ввести значение
    username_field = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")
    print("✓ Введен username: tomsmith")
    
    # Шаг 2: Найти поле password и ввести значение
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("✓ Введен пароль")
    
    # Шаг 3: Нажать кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("✓ Нажата кнопка Login")
    
    # Шаг 4: Дождаться появления зеленой плашки и получить её текст
    # Плашка успешного входа имеет класс 'success' и находится в div с id='flash'
    success_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.flash.success"))
    )
    
    # Получаем текст (и убираем символ '×' в конце, если он есть)
    message_text = success_message.text.replace('×', '').strip()
    
    # Шаг 5: Вывести текст в консоль
    print("\n" + "="*50)
    print("ТЕКСТ ЗЕЛЕНОЙ ПЛАШКИ:")
    print(message_text)
    print("="*50 + "\n")
    
    # Небольшая пауза, чтобы увидеть результат на странице
    time.sleep(2)

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрыть браузер
    driver.quit()
    print("Браузер закрыт")
