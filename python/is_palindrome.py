# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение
# True если указанный текст является палиндромом и False в противном случае.
#
def is_palindrome(str):
    str = str.replace(' ', '')
    str = str.replace(',', '')
    str = str.replace('-', '')
    str = str.replace('?', '')
    str = str.replace('.', '')
    str = str.replace('!', '')
    str = str.lower()
    list = []

    for i in range(len(str)):
        list.append(str[i])

    if list == list[::-1]:
        return True
    else:
        return False


str1 = input()

print(is_palindrome(str1))
