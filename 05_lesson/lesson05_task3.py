from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка драйвера Firefox (предполагается, что geckodriver установлен и в PATH)
driver = webdriver.Firefox()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Дать странице загрузиться
    driver.maximize_window()
    time.sleep(1)
    
    # Найти поле ввода (input с типом number)
    # Можно использовать несколько вариантов локаторов, выберем по тегу и типу
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
    )
    
    print("Поле ввода найдено")
    
    # Шаг 1: Ввести текст 12345
    input_field.send_keys("12345")
    print("✓ Введено: 12345")
    time.sleep(1)  # Пауза для наглядности
    
    # Шаг 2: Очистить поле (метод clear())
    input_field.clear()
    print("✓ Поле очищено")
    time.sleep(1)
    
    # Шаг 3: Ввести текст 54321
    input_field.send_keys("54321")
    print("✓ Введено: 54321")
    time.sleep(2)  # Пауза, чтобы увидеть результат
    
    print("Все действия выполнены успешно!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрыть браузер (метод quit())
    driver.quit()
    print("Браузер закрыт")
