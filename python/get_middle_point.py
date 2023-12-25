# Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка
# (x1:y1) и (x2:y2) и возвращает координаты точки являющейся серединой данного отрезка.


def get_middle_point(x1, y1, x2, y2):
    x3 = ((x1 + x2) / 2)
    y3 = ((y1 + y2) / 2)
    return x3, y3


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

x, y = get_middle_point(x1, y1, x2, y2)
print(x, y)
