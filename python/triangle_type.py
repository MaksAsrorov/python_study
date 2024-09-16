a = int(input())
b = int(input())
c = int(input())


if a == b == c:
    print("Равносторонний треугольник")
elif a == b or a == c or b == c:
    print("Равнобедренный треугольник")
elif a + b == c or a + c == b or b + c == a:
    print("Прямоугольный треугольник")
else:
    print("Разносторонний треугольник")
