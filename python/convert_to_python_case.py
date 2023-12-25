# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в
# «верблюжьем регистре» и преобразует его в «змеиный регистр».


def convert_to_python_case(text):
    counter = sum(1 for char in text if char.isupper())
    for i in range(counter):
        text += '@'

    for i in range(1, len(text)):
        if text[i].isupper():
            text = text.replace(text[i], '_' + text[i].lower())

    text = text.replace('@', '')
    if text[0] == '_':
        return text[1:]

    return (text.lower())


str1 = input()

print(convert_to_python_case(str1))
# ThisIsCamelCased
# IsHeFreeToGo
