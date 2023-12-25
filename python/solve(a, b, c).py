# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа
# a, b, c – коэффициенты квадратного уравнения  ax**2 +bx+c=0 и возвращает его корни в порядке возрастания.

from math import *


def solve(a, b, c):
    discriminant = b ** 2 - (4 * a * c)

    if discriminant == 0:
         return (-b / (2 * a)), (-b / (2 * a))

    else:
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return (x1, x2)


a, b, c = float(input()), float(input()), float(input())
x1, x2 = solve(a, b, c)

print(x1, x2)

