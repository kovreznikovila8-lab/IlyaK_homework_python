class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной
        и возвращает этот же текст
        Пример: `capitilize("skypro") -> "Skypro"`
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        whitespace = " "
        while string.startswith(whitespace):
            string = string[1:]  # Используем срез вместо removeprefix
        return string

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ
        и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        return symbol in string  # Простая и надёжная проверка

    def delete_symbol(self, string: str, symbol: str) -> str:
        return string.replace(symbol, "")

        # Ручное удаление всех вхождений (гарантированно работает)
        result = ""
        i = 0
        symbol_len = len(symbol)
        while i < len(string):
            if string[i:i+symbol_len] == symbol:
                i += symbol_len  # Пропускаем символ
            else:
                result += string[i]  # Добавляем символ в результат
                i += 1
        return result
