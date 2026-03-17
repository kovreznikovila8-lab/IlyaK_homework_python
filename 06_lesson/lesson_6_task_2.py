from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Настройка драйвера (для Chrome)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10) # Ожидание до 10 секунд

try:
    # 2. Перейти на страницу
    print("Переходим на страницу...")
    driver.get("http://uitestingplayground.com/textinput")

    # 3. Укажите в поле ввода текст SkyPro
    print("Вводим текст 'SkyPro' в поле...")
    # Ждем, когда поле станет доступным для ввода
    input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-control")))
    input_field.clear() # На всякий случай очищаем поле
    input_field.send_keys("SkyPro")

    # 4. Нажмите на синюю кнопку
    print("Нажимаем синюю кнопку...")
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
    button.click()

    # 5. Получите текст кнопки и выведите в консоль
    print("Получаем обновленный текст кнопки...")
    # Ждем, когда текст кнопки изменится с исходного ("Button") на введенный нами
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "button.btn-primary"), "SkyPro"))
    updated_button_text = button.text

    print("\nРезультат выполнения задания:")
    print(updated_button_text)

finally:
    # Закрыть браузер
    driver.quit()
    print("\nБраузер закрыт.")
