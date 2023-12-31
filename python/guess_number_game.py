# Описание проекта:
# программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
# Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
from random import *


# нужно проверить, что данные, которые ввел пользователь - валидны
def is_valid(x):
    if 1 <= x <= 100 :
        return True


def guess_number_game(x):
    number = randint(1, 100)

    if is_valid(x) == True:
        while x != number:
            if x < number:
                print("Слишком мало, попробуй еще раз!")
            if x > number:
                print("Слишком много, попробуйте еще раз")

            x = int(input())

            if x == number:
                print("Ты угадал, поздравляю!")
    else:
        print('Введите число от 1 до 100:')
        x = int(input())


print('Добро пожаловать в числовую угадайку')
print('Введи число:')

x = int(input())

print(guess_number_game(x))
