import math


def square(side):
    area = side * side
    if side % 1 != 0:
        area = math.ceil(area)
    return area


if __name__ == "__main__":
    print(square(5))
    print(square(5.0))
    print(square(5.1))
    print(square(4.9))
