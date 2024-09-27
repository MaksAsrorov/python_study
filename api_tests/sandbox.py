# numbers = list(map(int, input().split()))
# var = 0
# for i in numbers:
#     var += i
# print(var)

# students = ['Alex', 'Sveta', 'Lena', 'Igor', 'Svetlana']
#
# for i in students[3:]:
#         print(i)

# numbers = list(map(int, input().split()))
# var = 0
# for i in numbers:
#     if i % 2 == 0:
#         var += i
#     else:
#         continue
# print(var)


#
# films = input().split()
# var = 0
# for i in films:
#     print("Индекс " + str(var) + ": " + i)
#     var += 1


# numbers = list(map(int, input().split()))
# var = 0
# for i in numbers:
#     if var % 2 == 0:
#         print(i)
#     var += 1


# 1 2 3 4 5 6 7 8 9 10

# numbers = list(map(int, input().split()))
# var = 0
#
# for i in numbers:
#     var += i
# # print(var/len(numbers))
#
# a = input()
#
# var = 0
# for i in a:
#     if i == 'a' or i == 'b' or i == 'i':
#         var +=1
#     else:
#         continue
# print(var)

# a = []
#
# i =0
# b =1
#
# while i <10:
#     a.insert(i, b)
#     b +=1
#     i+=1
#
# for i in range(0,5):
#     print(a[i])


# numbers_1 = list(map(int, input().split()))
# numbers_2 = list(map(int, input().split()))
#
# var_1 = 0
# for i in numbers_1:
#     var_1 += i
#
# var_2 = 0
# for i in numbers_2:
#     var_2 += i
#
# if var_1 > var_2:
#     print("1")
# else:
#     print("2")

# # 1 3 2 1 4 10 5 3
# index_1 = 0
# index_2 = 1
# var = 0
#
# a = list(map(int, input().split()))
# # print(a[index_1])
# if a[index_1] > a[index_2]:
#     # print(a[index_1])
#     var = a[index_1]
# else:
#     # print(a[index_2])
#     var = a[index_2]
#
# index_2 = 2
#
# for i in a:
#     if var > a[index_2]:
#         print(var)
#     else:
#         print(a[index_2])
#     index_2 += 1


# a = int(input())
# res = 1
#
# for i in range (1, a+1):
#     # if i * 2 == 2:
#     #     res = (res * 2) - 1
#     # else:
#         res = res * 2
# print(res-1)



# # 01.12.2000 5.05.1992 11.11.2011 8.09.1521
#
# list = input().split()
#
# year = 0
# for i in list:
#     year = int(i[-4:])
#     if year % 4 == 0:
#         print(i)
#     else:
#         continue

#
# numbers = list(map(int, input().split()))
#
# a = 0
# while a < len(numbers):
#         if (numbers[a] % 2 == 1):
#             print(numbers[a]**2)
#             a += 1
#         else:
#             a += 1
#             continue
#

# list = input().split()
#
#
# a = 0
# while list[a].isalpha():
#     print(list[a])
#     a +=1
#
# a = (input())
# i = 0
#
# while i < len(a):
#     print(a[i])
#     i+=1
#
# a = int(input())
# i = 1
#
# while i+1 < a+2:
#     print(i)
#     i+=1

# numbers = list(map(int, input().split()))
# i = 0
# while i < len(numbers):
#     if numbers[i] >1:
#         print(numbers[i])
#     i += 1
#

# a = input()
# b = ""
# i = 0
# while a[i] != " " or i <30:
#     b += (a[i])
#     i += 1
# # print(b+"!")
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
#
# while i <= len(numbers):
#     if ((numbers[i] * numbers[i])+(numbers[i+1] * numbers[i+1])) >= 100 :
#         print(numbers[i])
#         print(numbers[i+1])
#         break
#     else:
#         i += 1
#         continue
#
#
#
# # and numbers[i+1] <= 10

#
# a = int(input())
# b = int(input())
# res = a - (a * 0.9)
# i = 0
#
# while a >= b:
#     i += 1
#     a = a - res
# print(i)

# a = input()
#
# res_1 = ""
#
# i = len(a) - 1
# while i >= 0:
#     res_1 += a[i]
#     i -= 1
#
# if a == res_1:
#     print("Good")
# else:
#     print("Bad")

#
# numbers = list(map(int, input().split()))
# i = 0
#
# while numbers[i] > 7:
#     print(numbers[i])
#     i+=1
#
#
#
# numbers = list(map(int, input().split()))
# i = 0
# per = 0
# vto = 0
# while i < len(numbers):
#     if numbers[i] > per:
#         per = numbers[i]
#         i += 1
#     else:
#         i += 1
#         continue
# print(per)
#
# i = 0
# while i < len(numbers):
#     if numbers[i]


# numbers = list(map(int, input().split()))

# i = 0
# per = 0
# counter = 0
# while i < len(numbers):
#     if numbers[i] > per:
#         per = numbers[i]
#         counter += 1
#         i += 1
#         print(per)
#         # if counter < 5:
#         #     print(per)
#         # else:
#         #     break
#     else:
#         i += 1
#         continue


# numbers = list(map(int, input().split()))
# res = (max(numbers))
# red = (min(numbers))
# i = 0
# list = []
# while i < len(numbers):
#     if numbers[i] < res and numbers[i] > red:
#         list.insert(0,numbers[i])
#         i += 1
#     else:
#         i += 1
#         continue
# print(max(list))
#
#
#

numbers = list(map(int, input().split()))
i = 0
res = 0

while i < len(numbers):
    if numbers[i] > 0:
        res += (numbers[i])
        i += 1
    else:
        i += 1
        continue
print(res)