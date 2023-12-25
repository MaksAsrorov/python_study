# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения:
# длину окружности и площадь круга, ограниченного данной окружностью.

import math


def get_circle(radius):
    length = 2 * math.pi * r
    square = math.pi * r ** 2
    return length, square


r = float(input())

length, square = get_circle(r)

print(length, square)
