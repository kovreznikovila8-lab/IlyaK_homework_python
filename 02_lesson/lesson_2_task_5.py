def month_to_season(month):

    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Неверный номер месяца"


if __name__ == "__main__":
    print(month_to_season(2))
    print(month_to_season(5))
    print(month_to_season(8))
    print(month_to_season(11))
    print(month_to_season(13))
