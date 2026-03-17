from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Настройка драйвера
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)  # Ожидание до 20 секунд

try:
    # 2. Перейти на страницу
    print("Переходим на страницу...")
    driver.get("http://uitestingplayground.com/ajax")

    # 3. Нажать на синюю кнопку
    print("Нажимаем синюю кнопку...")
    button = wait.until(EC.element_to_be_clickable((By.ID, "ajaxButton")))
    button.click()

    # 4. Получить текст из зеленой плашки
    print("Ожидаем появления зеленой плашки (до 15 секунд)...")
    # Явное ожидание появления элемента с текстом
    success_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success")))

    # Извлекаем текст
    result_text = success_label.text
    print(f"Получен текст: '{result_text}'")

    # 5. Вывести его в консоль (требуемая строка)
    print("\nРезультат выполнения задания:")
    print(result_text)

finally:
    # Закрыть браузер
    driver.quit()
    print("\nБраузер закрыт.")
