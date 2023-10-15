# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую
# из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной
# последовательностью и False в противном случае.


def is_correct_bracket(text):
    counter = 0
    for i in range(len(text)):
        if text[i] == '(':
            counter += 1
        if text[i] == ')':
            counter -= 1
        if counter < 0:
            return False

    if counter == 0:
        return True
    else:
        return False


str1 = input()

print(is_correct_bracket(str1))
