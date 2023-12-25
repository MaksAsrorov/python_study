# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
# фанатеет от математики, то он решил:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и
# возвращает значение True, если пароль является действительным паролем BEEGEEK банка и False - в противном случае.

def is_palindrome(str):
    list = []

    for i in range(len(str)):
        list.append(str[i])

    if list == list[::-1]:
        return True
    else:
        return False


def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if (num % i) == 0:
            counter += 1
    if counter > 2 or num <= 1:
        return False
    else:
        return True


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


password = input()
password_count = (password.count(":"))
password = password.split(':')

a = password[0]
b = int(password[1])
c = int(password[2])



def common_result():
    if password_count <= 2 and (is_palindrome(a) == True) and (is_prime(b) == True) and (is_even(c) == True):
        return True
    else:
        return False


print(common_result())
