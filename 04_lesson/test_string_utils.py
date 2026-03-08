import pytest
from string_utils import StringUtils


class TestStringUtils:
    """Класс с тестами для StringUtils"""

    # ========== ТЕСТЫ ДЛЯ МЕТОДА CAPITALIZE ==========

    @pytest.mark.parametrize("input_str, expected", [
        # Позитивные сценарии
        ("skypro", "Skypro"),                    # обычная строка
        ("hello world", "Hello world"),           # строка с пробелом
        ("123abc", "123abc"),                      # числа как строка
        ("04 апреля 2023", "04 апреля 2023"),      # строка с пробелами
        ("Тест", "Тест"),                           # не пустая строка
        ("а", "А"),                                 # один символ кириллицей
        # Негативные сценарии
        ("", ""),                                   # пустая строка
        (" ", " "),                                 # строка с пробелом
    ])
    def test_capitalize(self, input_str, expected):
        """Тесты capitalize: позитивные и негативные сценарии"""
        utils = StringUtils()
        assert utils.capitalize(input_str) == expected

    @pytest.mark.parametrize("input_str", [
        None,
        123,
        [],
        {},
        []
    ])
    def test_capitalize_invalid_types(self, input_str):
        """Негативные тесты capitalize: некорректные типы"""
        utils = StringUtils()
        with pytest.raises((AttributeError, TypeError)):
            utils.capitalize(input_str)

    # ========== ТЕСТЫ ДЛЯ МЕТОДА TRIM ==========

    @pytest.mark.parametrize("input_str, expected", [
        # Позитивные сценарии
        ("   skypro", "skypro"),                   # пробелы в начале
        ("skypro", "skypro"),                       # без пробелов
        ("   hello world", "hello world"),          # пробелы + пробел внутри
        ("   04 апреля 2023", "04 апреля 2023"),    # числа с пробелами
        ("   Тест", "Тест"),                         # кириллица
        # Негативные сценарии
        ("", ""),                                    # пустая строка
        (" ", ""),                                   # строка из одного пробела
        ("   ", ""),
        ("\t skypro", "\t skypro"),                  # табуляция (не удаляется)
    ])
    def test_trim(self, input_str, expected):
        """Тесты trim: удаление пробелов в начале"""
        utils = StringUtils()
        result = utils.trim(input_str)
        assert result == expected
        # Дополнительная проверка: результат не начинается с пробела
        if input_str.startswith(" "):
            assert not result.startswith(" ")

    def test_trim_none(self):
        """Негативный тест trim: передача None"""
        utils = StringUtils()
        with pytest.raises((AttributeError, TypeError)):
            utils.trim(None)

    # ========== ТЕСТЫ ДЛЯ МЕТОДА CONTAINS ==========

    @pytest.mark.parametrize("string, symbol, expected", [
        # Позитивные сценарии
        ("SkyPro", "S", True),                      # символ в начале
        ("SkyPro", "o", True),                       # символ в конце
        ("SkyPro", "yP", True),                      # подстрока
        ("Hello World", " ", True),                   # пробел
        ("Тест", "т", True),                          # кириллица
        ("04 апреля 2023", "апреля", True),           # слово с пробелами
        ("123", "2", True),                           # число как строка
        # Негативные сценарии
        ("", "", True),                               # пустая строка
        (" ", " ", True),                             # пробел + пробел
        ("SkyPro", "U", False),                       # символа нет
        ("Hello", "hello", False),                    # разный регистр
        ("SkyPro", "", True),                          # пустой символ
    ])
    def test_contains(self, string, symbol, expected):
        """Тесты contains: поиск символа/подстроки"""
        utils = StringUtils()
        assert utils.contains(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol", [
        ("SkyPro", None),
        (None, "S"),
        (123, "S"),
        ("SkyPro", 123),
        ([], "S"),
        ("SkyPro", []),
    ])
    def test_contains_invalid_types(self, string, symbol):
        """Негативные тесты contains: некорректные типы"""
        utils = StringUtils()
        with pytest.raises((TypeError, AttributeError)):
            utils.contains(string, symbol)

    # ========== ТЕСТЫ ДЛЯ МЕТОДА DELETE_SYMBOL ==========

    @pytest.mark.parametrize("string, symbol, expected", [
        # Позитивные сценарии
        ("SkyPro", "k", "SyPro"),                    # удаление символа
        ("SkyPro", "Pro", "Sky"),                     # удаление подстроки
        ("SkyPro", "y", "SkPro"),                      # символ в середине
        ("aaaaa", "a", ""),                            # все символы
        ("Тест", "т", "Тес"),                          # кириллица
        ("04 апреля 2023", "апреля", "04  2023"),      # удаление слова
        ("123", "2", "13"),                            # число как строка
        ("Hello World", " ", "HelloWorld"),            # удаление пробела
        # Негативные сценарии
        ("", "", ""),                                   # пустая строка
        (" ", " ", ""),                                 # пробел + пробел
        ("Hello", "x", "Hello"),                        # символ не найден
        ("SkyPro", "", "SkyPro"),                       # пустой символ
    ])
    def test_delete_symbol(self, string, symbol, expected):
        """Тесты delete_symbol: удаление подстрок"""
        utils = StringUtils()
        assert utils.delete_symbol(string, symbol) == expected

    def test_delete_symbol_multiple_occurrences(self):
        """Тест delete_symbol: множественные вхождения"""
        utils = StringUtils()

        result1 = utils.delete_symbol("abacaba", "a")
        assert result1 == "bcb"      # удаление всех 'a'

        result2 = utils.delete_symbol("abacaba", "b")
        assert result2 == "aacaa"    # удаление всех 'b'

        result3 = utils.delete_symbol("abacaba", "ab")
        assert result3 == "acaba"    # удаление подстроки 'ab'

        result4 = utils.delete_symbol("aaaaaa", "a")
        assert result4 == ""         # все символы удалены

        result5 = utils.delete_symbol("ababab", "ab")
        assert result5 == ""         # все подстроки удалены

    @pytest.mark.parametrize("string, symbol", [
        ("SkyPro", None),
        (None, "k"),
        (123, "k"),
        ("SkyPro", 123),
        ([], "k"),
        ("SkyPro", []),
    ])
    def test_delete_symbol_invalid_types(self, string, symbol):
        """Негативные тесты delete_symbol: некорректные типы"""
        utils = StringUtils()
        with pytest.raises((TypeError, AttributeError)):
            utils.delete_symbol(string, symbol)

    # ========== ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ ==========

    def test_contains_with_special_characters(self):
        """Тест contains: спецсимволы"""
        utils = StringUtils()
        assert utils.contains("Hello\nWorld", "\n") is True
        assert utils.contains("Hello\tWorld", "\t") is True
        assert utils.contains("Hello\\World", "\\") is True

    def test_delete_symbol_with_special_characters(self):
        """Тест delete_symbol: спецсимволы"""
        utils = StringUtils()
        assert utils.delete_symbol("Hello\nWorld", "\n") == "HelloWorld"
        assert utils.delete_symbol("Hello\tWorld", "\t") == "HelloWorld"
        assert utils.delete_symbol("Hello\\World", "\\") == "HelloWorld"

    def test_chain_operations(self):
        """Тест: последовательное применение методов"""
        utils = StringUtils()
        text = "   hello world"
        trimmed = utils.trim(text)
        assert trimmed == "hello world"

        capitalized = utils.capitalize(trimmed)
        assert capitalized == "Hello world"

        without_spaces = utils.delete_symbol(capitalized, " ")
        assert without_spaces == "Helloworld"
