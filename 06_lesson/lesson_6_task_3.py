from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Настройка драйвера
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15) # Увеличим таймаут до 15 секунд для загрузки картинок

try:
    # 2. Перейти на страницу
    print("Переходим на страницу...")
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    print("Ожидаем загрузки всех изображений...")

    # 3. Ждем загрузки всех картинок
    # На странице есть текст-индикатор, который исчезает после загрузки. Это хорошая точка ожидания.
    # Ждем, когда текст "Please wait..." исчезнет (станет невидимым)
    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    # Дополнительная страховка: ждем появления всех картинок (их должно быть не меньше 4)
    # Картинки находятся внутри div с ID "image-container" или просто по тегу img
    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img")))
    print(f"Найдено изображений: {len(images)}")

    # 4. Получить значение атрибута src у 3-й картинки
    # Индексация в Python начинается с 0, поэтому 3-я картинка имеет индекс 2
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print(f"\nSRC 3-й картинки: {third_image_src}")

        # 5. Вывести значение в консоль
        print("\nРезультат выполнения задания:")
        print(third_image_src)
    else:
        print(f"Ошибка: загрузилось только {len(images)} картинок, ожидалось минимум 3.")

finally:
    # Закрыть браузер
    driver.quit()
    print("\nБраузер закрыт.")
