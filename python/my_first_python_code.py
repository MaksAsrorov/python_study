# # a = int(input())
# # b = int(input())
# # while n>9:
# #     n = n//10 + n%10
# # print(n)
# #
# #///////
# # поиск делителей
# # n = int(input())
# # for i in range (1, n+1):
# #     if n%i==0:
# #        print(i)
# # a = int(input())
# # b = int(input())
# #
# # sum = 0
# # total = 0
# #
# # max_digit = 0
# #
# # for n in range (a, b+1):
# #       for k in range (1, n+1):
# #           if n%k==0:
# #             sum += k
# #       if sum >= total:
# #           total = sum
# #           max_digit = n
# #       sum = 0
# #
# # print(max_digit, total, end=' ')
# #
# #
# #
#
#
#
#
#
# n = int(input())
# for i in range (1, n+1):
#     if n%i==0:
#        print(i)
#

# s = 'All you need is love'
# if 'love' in s:
#     print('❤️')
# else:
#     print('💔')

# text = "Such a lovely place"
#
# for index in range(len(text)):
#     print(text[index])

# text = "Such a lovely place"
#
# for letter in text:
#     print(letter)

# alphabet = "abcdefghijk"
#
# for letter in alphabet:
#     print(letter)

# n = input()
#
# for index in range (-len(n), 0, 1):
#     print(n[index], index)
#

# На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.

# n = input()
# total = 0
#
# for index in range (0, len(n)):
#     total += int(n[index])
# print(total)


# n = input()
# counterX = 0
# counterP = 0
#
# for index in range (0, len(n)):
#     if n[index] == '*':
#         counterX += 1
#     if n[index] == '+':
#         counterP += 1
# print("Символ + встречается", counterP, "раз")
# print("Символ * встречается", counterX, "раз")
# n = input()
# counter = 0
#
# for index in range ((len(n)-1)):
#     if n[index]==n[index+1]:
#         counter+=1
# print(counter)

# завели счетчик
# - проходим for по len(строки) - 1
# - в if сравниваем строки[i] с строки[i + 1]
# - с новой строки выводим счетчик

# Количество гласных букв равно 25
# Количество согласных букв равно 24

# n =input()
# counter_g = 0
# counter_s = 0
#
# for index in range (0, len(n)):
#     if n[index] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         counter_g += 1
#     if n[index] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         counter_s +=1
#
# print('Количество гласных букв равно', counter_g)
# print('Количество согласных букв равно', counter_s)

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::])

# На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет является ли оно палиндромом.


#
# if s[:] == s[::-1]:
#     print('YES')
# else:
#     print('NO')

#
# На вход программе подается одна строка. Напишите программу, которая выводит:
#


# строку с удаленным первым и последним символом.


# s = input()
# #
# # # общее количество символов в строке;
# #
# total_digit = 0
# for index in range(0, len(s)):
#     total_digit +=1
# print(total_digit)
#
# # исходную строку, повторенную 3 раза;
# for i in range(0, 3):
#     print(s, end='')
#
# # первый символ строки;
# print('')
# print(s[0])
#
# # первые три символа строки;
# print(s[:3])
# #
# # последние три символа строки;
# print(s[-3:])
#
# # строку в обратном порядке;
# print(s[::-1])
#
# # строку с удаленным первым и последним символом.
# print(s[1:-1])
#
#
#
#
# s = input()

# # # третий символ этой строки;
# print(s[2])
# #
# # # предпоследний символ этой строки;
# print(s[-2])
# #
# # # первые пять символов этой строки;
# print(s[:5])
# #
# # # всю строку, кроме последних двух символов;
# print(s[:-2])
# #
# # # все символы с четными индексами;
# print(s[::2])
# #
# # # все символы с нечетными индексами;
# for index in range (0, len(s)):
#     if index%2==1:
#         print(s[index], end='')
#
# # # все символы в обратном порядке;
# print('')
# print(s[::-1])

# все символы строки через один в обратном порядке, начиная с последнего.
# print(s[::-2])

# s = input()
#
# if len(s)%2==0:
#     print((s[(len(s)//2):]) + (s[:(len(s)//2)]))
# else:
#     print((s[(len(s)//2)+1:]) + (s[:(len(s)//2)+1]))

# На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом.
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
#

# s = 'Максим Асроров'
#
# if s == s.title():
#     print("YES")
# else:
#     print("NO")

# s = input()
#
# print(s.swapcase())

# На вход программе подается строка текста.
# Напишите программу, которая определяет является ли оттенок текста хорошим или нет.
# Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.
#
# s = input()
#
# # for index in range(0, len(s)):
# if 'хорош' in s.lower():
#     print('YES')
# else:
#     print('NO')

# я очень хороший текст =)

# На вход программе подается строка.
# Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.

# s = input()
# counter = 0
#
# for index in range (0, len(s)):
#     if s[index] == s[index].lower() and s[index] not in '1234567890':
#         counter +=1
#
# print(counter)

# s = input()
# print(s.count(' ')+1)

# На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин).
# Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
#
# Аденин: 3
# Гуанин: 2
# Цитозин: 3
# Тимин: 5
# АааГГЦЦцТТттт

# s = input().lower()
# print('Аденин:',  s.count('а'))
# print('Гуанин:',  s.count('г'))
# print('Цитозин:',  s.count('ц'))
# print('Тимин:',  s.count('т'))

# Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему поступает n различных последовательностей кода Морзе.
# Декодировав их, он получает последовательности из цифр и строчного латинского алфавита, при этом во всех сообщениях Оди содержится число 11,
# причем минимум 3 раза. Помогите определить Джиму количество сообщений от Оди

# n = int(input())
# counter = 0
#
# for i in range (0, n):
#     s = input()
#     if s.count('11') == 3:
#         counter += 1
# print(counter)

# На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
# s = input()
# counter = 0
#
# for index in range(0, len(s)):
#     if s[index] in '0123456789':
#         counter +=1
# print(counter)
#


# s = input()
#
# if s.endswith('.ru') or s.endswith('.com'):
#     print("YES")
# else:
#     print("NO")


# На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке, разделенных символом пробела.
# Если буква «f» в данной строке не встречается, следует вывести «NO».

# s = input()
# counter = s.count('f')
#
# if counter == 0:
#     print("NO")
# if counter == 1:
#     print(s.index('f'))
# if counter >= 2:
#     print((s.find('f')), (s.rfind('f')), end=' ')


# На вход программе подается строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.

# s = input()
# print((s[:s.find('h')]) + (s[s.rfind('h')+1:]))

# На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.

# aaaabbc

# s = input()
# total = 0
# str_total = ''
#
# for c in s:
#     if s.count(c) >= total:
#         total = s.count(c)
#         str_total = c
# print(str_total)

# first_name = 'Максим'
# last_name = 'Асроров'
# age = '31'
# profession = 'engineer'
# affiliation = 'BeeGeek'
# print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')

# In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек)#
# year = 2010
# total = '10k'
# what = 'Bitcoin'
# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, total, what)
#
# print(s)


# for i in range (int(input()), int(input())+1):
#     print(chr(i), end='')

# s = input()
# for index in s:
#     print(ord(index), end=' ')

#
# n = int(input())
#
#
# for i in input():
#     decryption = (ord(i) - n)
#     if decryption < 97:
#         decryption += 26
#     print(chr(decryption), end='')

# s = 'Python rocks!'
# d=''
#
# for i in range (0, len(s)):
#     if i%3!=0:
#         d += s[i].replace(s[i], '')
# print(d)

# print(input().replace('@', ''))
# s = input()
# counter = 0
# #
# for i in s:
#     if i == 'f':
#         counter += 1
# if counter == 1:
#     print(-1)
# if counter == 0:
#     print(-2)
# if counter >=2:
#     d = s.replace('f', 'd', 1)
#     print(d.find('f'))


# s = 'abch54321h'
#
# # for index in range (0, len(s)):
# df = s.find('h')
# dl = s.rfind('h')
# temp = (s[df:dl])
# print(s[:df+1]+temp[::-1]+s[dl+1:])


# numbers = [2, 4, 6, 8, 10]
# languages = ['Python', 'C#', 'C++', 'Java']
# print(numbers)
# print(languages)

# numbers = list(range(1, int(input())+1))
# print(chr(numbers))


#
# print(ord('a'))
# (97, 122)

# numbers = list(range(1, int(input())+1))
# n = int(input())
# for i in range (0, n+1):
# numbers = chr(list(range(97, 123)))

# print(list(range(97, int(input())+97)))
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#
#
# if ("Green" in rainbow):
#     index = rainbow.index("Green")
#     rainbow[index] = "Зеленый"
#
# if ("Violet" in rainbow):
#     index = rainbow.index("Violet")
#     rainbow[index] = "Фиолетовый"
#
# print(rainbow)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#
# rainbow[3] ='Зеленый'
# rainbow[-1] ='Фиолетовый'
#
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])
#
# ополните приведенный код, используя операторы конкатенации (+) и умножения списка на число (*), так чтобы он вывел список:
#
#  [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13].

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(numbers1+numbers1 + (numbers2*9) + numbers3)

#
# numbers = [1, 1, 2, 3, 5, 8, 13]  # создаем список
#
# numbers.append(21)  # добавляем число 21 в конец списка
# numbers.append(34)  # добавляем число 34 в конец списка
#
# print(numbers)
#
# numbers = [0, 2, 4, 6, 8, 10]
# odds = [1, 3, 5, 7]
#
# numbers.extend(odds)
# print(numbers)

#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[5]    # удаляем элемент имеющий индекс 5
#
# print(numbers)


# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

# print(len(numbers)) #количество элементов
# print((numbers[-1])) #последний элемент списка
# print(numbers[::-1]) #список наоборот
#
# if 5 in numbers and 17 in numbers:
#     print('YES')
# else:
#     print("NO")
#
# del numbers[0]
# del numbers[-1]
#
# print(numbers)


# massive = []
#
# for i in range(0, (int(input()))):
#     s = input()
#     massive.append(s)
#
# print(massive)

# abc = 'abcdefghijklmnopqrstuvwxyz'
# massive = []
# massive2 = []
#
# for i in range(len(abc)):
#     massive = abc[i] * (i + 1)
#     massive2.append(massive)
# print(massive2)


# n = int(input())  # количество цифр которое нужно возвести в 3 степень
# massive = []
#
# for i in range(0, n):
#     massive.append(int(input()) ** 3)
# print(massive)

# n = int(input())
# massive = []
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         massive.append(i)
# print(massive)

# На вход программе подается натуральное число n
# n целых чисел. Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (

# n = int(input())
# sp1 = []
# sp2 = []
#
# for i in range(n):
#     sp1.append(int(input()))
# for i in range (len(sp1) - 1):
#     sp2.append((sp1[i] + sp1 [i + 1]))
# print(sp2)


# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список,
# затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.


# sp1 = []
# sp2 = []
# for i in range(0, int(input())):
#     sp1.append(int(input()))
#     if i%2==0:
#         sp2.append(sp1[i])
#
# print(sp2)

# sp1 = []
#
# for i in range(0, int(input())):
#     sp1.append(int(input()))
#
# del sp1[1::2]
#
# print(sp1)

# На вход программе подается натуральное число
# n, а затем
# n строк. Напишите программу, которая создает список из символов всех строк, а затем выводит его.

# n = int(input())
# sp1 = []
#
# for i in range(0, n):
#    sp1.extend(input())
# print(sp1)

# На вход программе подается натуральное число
# n и
# n строк, а затем число
# k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.
#

# n = int(input())
# sp1 = []
# sp2 = []
# sp3 = []
# for i in range(0, n):
#    sp1.extend(input())
# k = int(input())
#
# for c in range (0, len(sp1)):
#     sp2.extend(sp1)
#
# print(sp1)


# n = 'sjakdfkjsdhk'
#
# print(n[2])

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers)


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers, sep='\n')

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# total = 0
# for i in numbers:
#     total += i**2
# print(total)
# #

# n = int(input())
# sp1 = []
# sp2 = []
#
# for i in range (0, n):
#     x = int(input())
#     sp1.append(x)
#     sp2.append((x**2)+2*x+1)
#
# print(*sp1, sep='\n')
# print()
# print(*sp2, sep='\n')


# n = int(input())
# sp1 = []


# for i in range (0, n):
#     sp1.append(int(input()))
#
# sp1.remove(max(sp1))
# sp1.remove(min(sp1))
#
# print(*sp1, sep='\n')
#
# n = int(input())
# sp1 = []

# Как-то легко решил эту задачу. Сам удивлен.


# n = int(input())
# sp1 = []
#
# for i in range (n):
#     str = input()
#     if str not in sp1:
#         sp1.append(str)
#
# print(*sp1, sep='\n')


# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

#
# n = int(input())
# sp1 = []
# sp2 = []
#
# for i in range (n):
#     sp1.append(input())
#
# if input() in sp1:
#     for c in range (n):
#         sp2.append(sp1[c])


# print(sp2)
#
#
# n = int(input())
# sp1 = []
# sp2 = []
# sp3 = []
#
# for i in range(n):
#     sp1.append(input())
#
# x = input()
# for c in range(len(sp1)):
#     sp3.append(sp1[c].lower())
#     if sp3[c].find(x.lower()) != -1:
#         sp2.append(sp1[c])
# print(*sp2, sep='\n')


# n = int(input())
# sp1 = []
#
#
# for i in range(n):
#     sp1.append(int(input()))
#
# sp1.sort()
#
# print(*sp1, sep='\n')


# Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке.
# Числа должны быть выведены в том же порядке, в котором они были введены.

# n = int(input())
# sp = []
# so = []
# s0 = []
#
#
# for i in range(n):
#     x = int(input())
#     if x > 0:
#         sp.append(x)
#     if x < 0:
#         so.append(x)
#     if x == 0:
#         s0.append(x)
#
# print(*(so + s0 + sp), sep='\n' )


# n = int(input())
# sp1 = []
# sp2 = []
# sp3 = []
#
# for i in range (n):
#      sp1.append(input())
#
# x = input()
# for c in range (len(sp1)):
#     sp3.append(sp1[c].lower())
#     if sp3[c].find(x.lower()) != -1:
#          sp2.append(sp1[c])
# print(*sp2, sep='\n')
#

# n = int(input())
# a, b, c = [], [], []
# for i in range(n):
#     a.append(input())
# k = int(input())
# for j in range(k):
#     b.append(input())
# for h in range(len(a)):
#     count = 0
#     for g in range (len(b)):
#         if b[g].lower() in a[h].lower():
#             count += 1
#     if count == len(b):
#         c.append(a[h])
# print(*c, sep='\n')

# numbers = input().split('.')
# counter = 0
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#     if 256 > (numbers[i]) >= 0:
#         counter += 1
# if counter == 4:
#     print('ДА')
# else:
#     print('НЕТ')

#
# words = input()
# s = input().join(words)
# print(s)


# def draw_box():
#     print('*' * 10)
#     for i in range (0, 13):
#         print('*        *')
#     print('*' * 10)
#
# draw_box()
#
# # объявление функции
# def draw_triangle():
#     for i in range (11):
#         print('*' * i)

# основная программа
# draw_triangle()  # вызов функции

# def draw_triangle(fill, base):  # функция принимает два параметра
# base = base//2
# for i in range(base + 1):
#     print(fill * i)
#
# for i in range(base + 1, 0, -1):
#     print(fill * i)
#
# draw_triangle(input(), int(input()))
#
# name = input()
# familia = input()
# ot = input()
#
# print(familia[0].upper(), end='')
# print(name[0].upper(), end='')
# print(ot[0].upper(), end='')


# объявление функции
# def print_fio(name, surname, patronymic):
#     print(name[0].upper(), end='')
#     print(surname[0].upper(), end='')
#     print(patronymic[0].upper(), end='')
#
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(surname, name, patronymic)

# # объявление функции
# def print_digit_sum(num):
#     counter = 0
#     while num > 0:
#         counter += (num % 10)
#         num //= 10
#     print(counter)
#
#
# # # считываем данные
# n = int(input())
# #
# # # вызываем функцию
# print_digit_sum(n)

# # объявление функции
# def convert_to_miles(km):
#     miles = km * 0.6214
#     return miles
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))


# # объявление функции
# def get_days(month):
#     months_31 = [1, 3, 5, 7, 8, 10, 12]
#     months_30 = [4, 6, 9, 11]
#     months_28 = [2]
#
#     if month in months_31:
#         return 31
#     elif month in months_30:
#         return 30
#     elif month in months_28:
#         return 28
#
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(get_days(num))

#
# n = int(input())  # количество цифр которое нужно возвести в 3 степень
# massive = []
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         massive.append(i)
# print(massive)


# объявление функции
# def get_factors(num):
#     massive = []
#     counter = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             counter += 1
#     return counter
#
# считываем данные
# n = int(input())
#
# вызываем функцию
# print(get_factors(n))


# # объявление функции
# def find_all(target, symbol):
#     stri = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             stri.append(i)
#     return stri
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))


# # # объявление функции
# def merge(list1, list2):
#     list3 = list2 + list1
#     list3.sort()
#     return list3
#
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))

# list = [5, 4, 3, 2, 1]
# list.sort()
# print(list)

# def quick_merge2(list1, list2):
#     list3 = list2 + list1
#     list3.sort()
#     return list3
#
#
# total_list = []
#
# for i in range(int(input())):
#     num = [int(q) for q in input().split()]
#     total_list = quick_merge2(total_list, num)
# print(*total_list)


# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if ((side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)):
#         return True
#     else:
#         return False
#
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))


# def get_factors(num):
#     for i in range(1, n+1):
#         if  n > 1:
#             return False
#         else:
#             return True
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))

# если оно больше 1 и при этом делится без остатка только на 1 и на x

# n = int(input())

# flag = True
# for i in range (1, n+1):
#     if n > 1 and i % n ==0:
#         flag = True
#     else:
#         flag = False

# print(n/1)
# print(n/n)

# n = int(input())


# def is_prime(num):
#     counter = 0
#     for i in range(1, n + 1):
#         if (n % i) == 0:
#             counter += 1
#     if counter > 2 or n <= 1:
#         return False
#     else:
#         return True
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))


# # первое простое число большее числа num
# def is_prime_next(num):
#     counter = 0
#     while counter <= 0:
#
#         counter = 0
#         for i in range(1, n + 1):
#             if (n % i) == 0:
#                 counter += 1
#
#     if (num + 1) % (num + 1) == 0:
#         counter += 1
#     num += 1
#
#
#
# # считываем данные
#
#
# n = int(input())
#
# # вызываем функцию
# print(is_prime_next(n))


# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
# возвращает значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе и False  в противном случае.


# def is_one_away(word1, word2):
#     counter = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 counter += 1
#     else:
#         return False
#
#     if counter >= 2 or counter ==0:
#         return False
#     else:
#         return True
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))

#
# def is_my_first_function(a):
#     counter_1 = 0
#     counter_2 = 0
#     counter_3 = 0
#     if len(a) >= 8:
#         for i in range(len(a)):
#             if 90 >= ord(a[i]) >= 65:  # проверяем, есть ли буквы в верхнем регистре
#                 counter_1 += 1
#             if 122 >= ord(a[i]) >= 97:  # проверяем, есть ли буквы в нижнем регистре
#                 counter_2 += 10
#             if 57 >= ord(a[i]) >= 48:  # проверяем, есть ли цифра
#                 counter_3 += 100
#     if counter_1 != 0 and counter_2 != 0 and counter_3 !=0:
#         return True
#     else:
#         return False
#
# password = input()
# print(is_my_first_function(password))

# функция определяет является ли число простым или нет.

def is_prime_next(num):
    counter = 0
    for i in range(1, num + 1):
        if (num % i) == 0:
            counter += 1
    if counter > 2 or num <= 1:
        return False
    else:
        return True

# считываем данные
c = int(input())
c += 1

# # вызываем функцию
while is_prime_next(c) != True:
    c += 1
print(c)

