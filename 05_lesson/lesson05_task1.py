from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка драйвера (предполагается, что ChromeDriver в PATH или в папке проекта)
driver = webdriver.Chrome()

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")
    
    # Дать странице полностью загрузиться
    driver.maximize_window()
    time.sleep(2)
    
    # ------------------- ВАШ КОД ДЛЯ КЛИКА -------------------
    # Явное ожидание появления кнопки с классом 'btn-primary'
    # Используем XPath, который рекомендован на самой странице (в исходном коде):
    # //button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]
    
    wait = WebDriverWait(driver, 10)
    primary_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        )
    )
    
    # Кликнуть по кнопке
    primary_button.click()
    print("✓ Кнопка нажата, появился alert")
    
    # Подтвердить alert (нажать ОК)
    alert = driver.switch_to.alert
    alert.accept()
    print("✓ Alert принят")
    # ---------------------------------------------------------
    
    # Небольшая пауза, чтобы увидеть результат
    time.sleep(2)
    
    print("Скрипт выполнен успешно!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрыть браузер
    driver.quit()
