from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка драйвера
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    
    # Дать странице загрузиться
    driver.maximize_window()
    time.sleep(1)
    
    # ------------------- ВАШ КОД ДЛЯ КЛИКА -------------------
    # Используем надежный локатор, который не зависит от динамического ID
    # Вариант 1: По тексту кнопки (самый простой и надежный)
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Button with Dynamic ID']"))
    )
    
    # Альтернативный вариант 2: По классу (если текст вдруг изменится)
    # button = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
    # )
    
    # Кликнуть по кнопке
    button.click()
    print("✓ Кнопка с динамическим ID успешно нажата")
    # ---------------------------------------------------------
    
    # Небольшая пауза, чтобы увидеть результат
    time.sleep(2)
    
    print("Скрипт выполнен успешно!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрыть браузер
    driver.quit()
