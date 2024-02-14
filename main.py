# # name = "Elena"  # инициализация
# # print("Hello,", name)
# age = 20.4
# print(age)
# text = "Hello "
# print(text)
# print(text + str(age))
# print(type(age))  # int - 20 , float - 20.4
# print(type(text))  # str - "Hello"
# a = False  # True
# print(a)
# print(type(a))  # bool - True, False

# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))

# # множественное присваивание
# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# _name_6 = "Igor"
# name_new = "Igor"
# print(name_new)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 10
# b = 20
# print("a:", a)
# print("b:", b)
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка \n     символов D:\\folder\\file.txt')

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# # print(s1, ",", s2, "!")
# print(s3)
# print(s3 * 5)

# print(378475836832580280396556427956)
# print(3.78475836832580280396556427956)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(6 / 4)  # 1.4
# print(6 // 2)  # 3
# print(6 // 4)  # 1
# print(6 ** 2)  # степень
# print(6 % 2)  # остаток от деления

# # HomeWork
# a = 5
# b = 7
# c = 3
# print("Сумма:", a + b + c)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", ((a + b + c)//3))

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)  # 113 без скобок

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
# num -= 3  # num = num - 3
# print(num)  # 12

# num = 4325  # => 432
# print("Исходное число:", num)
# a = num % 10
# print(a)  # 5
# num //= 10
# # print(num)  # 432
# b = num % 10
# print(b)  # 2
# num //= 10
# # print(num)  # 43
# c = num % 10
# print(c)  # 3
# num //= 10
# # print(num)  # 4
# d = num % 10
# print(d)  # 4
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4325  # => 432
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10  # 432
# res += num % 10 * 100  # 5000 = 5000 + 432 % 10 => 5000 + 2 * 100 = 5200
# num //= 10  # 43
# print(num)
# res += num % 10 * 10  # 5200 = 5200 + 43 % 10 => 5200 + 3 * 10 = 5230
# num //= 10  # 4
# print(num)
# res += num  # 5230 = 5230 + 4
# print(res)

# num1 = "2.3"
# num2 = 3
# # res = num1 + str(num2)  # 23 (число целое берет)
# res = int(num1) + num2  # 5 (число целое берет)
# res = float(num1) + num2  # 5.3 (число берет полное)
# print(res)

# print(int(3.8))
# print(round(3.855, 1))
# print(type(round(3.891, 2)))

# name = "Виктор"
# age = 28
# print("Меня зовут " + name + ". Мне " + str(age) + "лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="  ")
# print("Я vxe Python.", end=" ")
# print("Я учу Python.")

# # name = input("Введите имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# # False => "", 0, False, None
# print(bool("python"))
# print(bool(""))
# print(bool(5))
# print(bool(-0.2))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# test = None
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 7)
# print(8 > 5)
# print(8 < 5)
# print(9 <= 9)
# print("привет" > "ПРИВЕТ")

# print(2 < 4 < 9)  # 2 < 4 < 9 => True && True => True
# print(2 * 5 > 7 >= 4 + 3)  # True && True => True
# print(3 * 3 <= 7 >= 2)  # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False:True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False:False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False:True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False:False)

# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)

# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("ВВедите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует")


# # HomeWork
# month = int(input("ВВедите номер месяца: "))
# if 1 <= month <= 12:
#     # print("Время года - ", end="")
#     if month == 12 or month == 1 or month == 2:
#         print("Зима")
#     if 3 <= month <= 5:
#         print("Весна")
#     if 6 <= month <= 8:
#         print("Лето")
#     if 9 <= month <= 11:
#         print("Осень")
# else:
#     print("Ошибка ввода данных")


# bird = int(input("Введите число ворон на ветке в диапазоне от 0 до 9: "))
# if 0 <= bird <= 9:
#     if bird == 1:
#         print("Ворона")
#     if 2 <= bird <= 4:
#         print("Вороны")
#     if 5 <= bird <= 9 or bird == 0:
#         print("Ворон")
# else:
#     print("Введите корректное значение")

# n = int(input("Введите количество ворон: "))
# a = "a"
# b = "ы"
# if 0 <= n <= 9:
#     print("На ветке " + str(n) + " ворон", end="")
#     if n == 1:
#         print(a)
#     if 2 <= n <= 4:
#         print(b)
# else:
#     print("Ошибка ввода данных")

# password = "admin"
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Логин не найден")

# day = 'вторник'
# time = 14
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 13 or 15 <= time <= 16:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 10, 20
# print(a if a < b else b)

# if a < b:
#     print(a)
# else:
#     print(b)

# a, b = 30, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = 10
# b = 0
# print("На ноль делить нельзя" if b == 0 else a / b)

# a = int(input("Введите числитель: "))
# b = int(input("Введите знаменатель: "))
# print('Результат: ', a / b if b else 'На ноль делить нельзя')

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
# print("Следующая строка")

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('Нельзя вводить строки')
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('Нельзя вводить строки или нельзя делить на ноль')
# else:  # когда в блоке try не возникло исключение (except)
#     print('Все нормально. Вы ввели числа', n, 'и', m)
# finally:  # выполнится в любом случае
#     print("Конец программы")

# n = input('Введите первое число: ')
# m = input('Введите второе число: ')
# try:
#     n = int(n)  # n = 5
#     m = int(m)  # m = два
# except ValueError:
#     n = str(n)  # n = '5'
# finally:
#     print(n + m)  # '5' + 'два'

# n = input('Введите первое число: ')
# m = input('Введите второе число: ')
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + str(m))


# ЦИКЛЫ

# while

# i = 0
# while i < 5:
#     print('i =', i)
#     i += 1  # i = i + 1

# i = 10
# while i > 0:
#     print('i =', i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print('i =', i)
#     i += 1

# i = 2
# while i <= 20:
#     print('i =', i)
#     i += 2

# n = int(input('Введите количество символов: '))
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1

# n = int(input('Введите количество символов: '))
# print('*' * n)
# print("*\n" * n)

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# res = 0
# while a <= b:  # 5 6 7 8 9 10
#     if a % 2:  # a % 2 != 0
#         res += a
#     a += 1
# print(res)  # 21

# HomeWork
# a = int(input('Введите количество символов: '))
# b = input('Введите тип символа: ')
# c = int(input('0 - горизонтальная, \n1 - вертикальная \nВведите ориентацию линии: '))
# i = 0
# while i < a:
#     if c == 0:
#         print(b, end=" ")
#     if c == 1:
#         print(b)
#     i += 1

# n = input("Введите число: ")
# while (type(n)) != int and (type(n)) != float:
#     try:
#         n = int(n)  # 7
#     except ValueError:
#         try:
#             n = float(n)
#         except ValueError:
#             print('Число не целое и не вещественное!')
#             n = input("Введите число: ")  # '7'
# # при такой задаче нижняя часть не актуальна
# if n % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input('Введите положительное число: '))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите положительное или отрицательное число: "))
#     if n == 0:
#         break
#     res *= n
# print('Результат: ', res)

# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i, end='')
#     i += 1
# else:
#     print("\nЦикл окончен, i =", i)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j=', j)
#         j += 1
#     i += 1

# Таблица умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("^", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1


# for element in collection:
#    print(element)

# for i in "Hello", "World", "!":
#     print(i)

# for element in range(n):
#    print(element)

# print(list(range(5)))

# range(start, stop, step)  # start=0  step=1

# for i in range(9):
#     print(i, end=" ")
#
# print()
#
# i = 9
# while i > 0:
#     print(i, end=" ")
#     i -= 2

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100 + 1):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# HomeWork
# count = 1
# while True:
#     res = 77
#     n = int(input("Введите число от 1 до 100: "))
#     if n < res and n != 0:
#         print("Загаданное число меньше")
#     if n > res:
#         print("Загаданное число больше")
#     if n == res:
#         print("Вы угадали загаданное число c", count, "раза")
#         break
#     elif n == 0:
#         print("Вы вышли из программы")
#         break
#     count += 1

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")


# for i in range(3):
#     print("+++ i =", i)
#     for j in range(2):
#         print("------ j=", j)

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# nums = [letter * 2 for letter in "Banana"]
# nums = [a for a in range(30) if a % 2 != 0]
# print(nums)


# Список (list)

# nums = [8, 3, 9, 4, 1, "one"]
# print(nums)
# print(type(nums))
#
# print(nums[0])
# print(nums[2])
# # print(nums[6])  # IndexError
# print(nums[-1])
# print(nums[-2])
#
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)

# nums = [8, 3, 9, 4, 1]
# print(nums)
#
# print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] ** 2, end=" ")

# s = []
# print(s)
#
# b = list("Hello")  # "Hello" => []
# print(b)
# print(b[0])

# a = 5
# print(int("3") + a)

# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(2, 10 + 1)))
# print(list(range(2, 10, 2)))


# [выражение for переменная in последовательность]
# a = [0 for _ in range(5)]
# print(a)

# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)

# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3  # вывели три раза переменную b
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)

# a = [int(input("Введите элемент: ")) for i in range(int(input("Введите количество элементов списка: ")))]
# res = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         res += a[i]
# print("Сумма отрицательных элементов: ", res)

# a = [int(input("Введите элемент: ")) for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)
# res = 0
# for i in a:
#     if i < 0:
#         res += i
# print("Сумма отрицательных элементов: ", res)

# a = list(range(10, 100, 10))
# print(a)
# for i in range(len(a)):
#     print(a[i] + 2, end=" ")
# print()
# for i in a:
#     print(i + 2, end=" ")

# a = [int(input("Введите элемент: ")) for i in range(int(input("Введите количество элементов списка: ")))]
# print("Сумма отрицательных элементов: ", sum([i for i in a if i < 0]))


# a = list(range(21, 40 + 1))
# print(a)
# count = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         count += 1
# print("Количество четных элементов списка: ", count)
# print("Сумма нечетных элементов: ", sum([i for i in a if i % 2 != 0]))

# a = list(range(21, 40 + 1))
# print(a)
# s = count = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         count += 1
#     else:
#         s += a[i]
# print("Количество четных элементов списка: ", count)
# print("Сумма нечетных элементов: ", s)

# a = list(range(21, 40 + 1))
# print(a)
# s = count = 0
# for i in a:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print("Количество четных элементов списка: ", count)
# print("Сумма нечетных элементов: ", s)


# n = list(range(21, 41))
# print(n)
# a = 2
# print(n[a])
# print(n[a-1])
# print(n[a+1])

# a = [int(input("Введите элементы списка: ")) for i in range(int(input("Введите количество элементов списка: ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")

# HomeWork
# a = [int(input("Введите элементы списка: ")) for i in range(int(input("Введите количество элементов списка: ")))]
# count = 0
# for i in a:
#     if i != 0:
#         count += 1
# print("Среднее арифметическое: ", sum([i for i in a])/count)

# a = [int(input("Введите элементы списка: ")) for i in range(int(input("Введите количество элементов списка: ")))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")


#  Срез
#  список [start:stop:step]

# a = [7, 8, 2, 1, 17, 9]
# print(a)
# # a[0], a[1] = a[1], a[0]
# # print(a)
# # print(a[1:4])  # [8, 2, 1] четвертый индекс не включается
# # print(a[1:])  # [8, 2, 1, 17, 9]
# # print(a[:3])  # [7, 8, 2]
# # print(a[::-1])  # [9, 17, 1, 2, 8, 7]
# print(a[5:2:-1])  # [9, 17, 1]
# print(a[10:20])  # []

# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# # s[4:] = []
# # print(s)
# # s[2:5] = []
# # print(s)
# # del s[1]
# del s[2:5]
# del s[:]
# print(s)

#  Методы списков

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет один элемент в конец списка [5, 9, 3, 7, 1, 8, 99]
# print(s)
# s.extend([1, 2, 3])  # добавляет список элементов в конец списка [5, 9, 3, 7, 1, 8, 99, 1, 2, 3]
# print(s)
# s.extend(["add"])  # добавляет элемент в конец списка [5, 9, 3, 7, 1, 8, 99, 1, 2, 3, 'add']
# print(s)
# s.insert(0, 100)  # добавляет элемент в заданный индекс, сам элемент передается вторым параметром
# print(s)
# s.insert(20, 200)  # добавляет элемент в последний индекс, если указать несуществующий индекс
# print(s)
# s.insert(len(s), 200)  # добавляет элемент в последний индекс, если указать len
# print(s)

# s = []
# n = int(input("Количество элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s)

# s = []
# n = int(input("Количество элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s[::-1])

# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)  # [2, 1, 4, 3]

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for element in a:
#     if element not in c and element in b:  # if True and True
#         c.append(element)
# print(c)  # [2, 1, 4, 3]

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # 3 4
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # 3 4
#         c.append(a[i])
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
#     for i in range(len(a)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # 3 4
#         c.append(b[i])
# print(c)

# s = [5, 9, 3, 7, 1, 8, 9, 1, 8, 9]
# print(s)
# s.remove(9)  # удаляет один элемент по заданному значению
# print(s)
# s.pop()  # удаляет один последний элемент из списка (если не указан параметр)
# print(s)
# a = s.pop(-1)  # передаем индекс для удаления элемента
# print(a)
# print(s)
# print(s.pop(1))  # удаляет один элемент из списка по индексу и возвращает его
# print(s)
# s.clear()  # очистка всех элементов списка
# print(s)


# s = []
# n = int(input("Введите элементы списка: \nn = "))
# for num in range(n):
#     x = int(input("-> "))
#     s.append(x)
# k = int(input("Введите индекс: \nk = "))
# a = s.pop(k)
# print(a)
# print(s)

# n = [int(input("-> ")) for i in range(int(input("Введите элементы списка: \nn = ")))]
# k = int(input("Введите индекс: \nk = "))
# n.pop(k)
# print(n)

# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# num = s.count(9)  # считает количество заданных значений в списке
# print(num)
#
# a = 9
# if a in s:
#     ind = s.index(9)  # возвращает индекс первого искомого элемента
#     print(ind)
# else:
#     print("Элемента", a, "не существует в списке")
#
# ind = s.index(9, 2)
# print(ind)


# HomeWork
# elem = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(elem)
# s = []
# for i in elem:
#     a = 0
#     for j in elem:
#         if i == j:
#             a += 1
#     if a == 1:
#         s.append(i)
# print(s)

# elem = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(elem)
# s = []
# for i in elem:
#     if elem.count(i) == 1:
#         s.append(i)
# print(*s)

# a = [1, 2, 3]
# b = a.copy()  # копирует объект в другую область памяти и возвращает копию
# print("a =", a)
# print("b =", b)
# a.append(20)
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)

# a = [5, 4, 1, 2, 3, ]
# print(a)
# # a.reverse()  # перестраивает элементы списка в обратном порядке
# # print(a)
#
# # a.sort()  # сортировка элементов списка
# # print(a)
# a.sort(reverse=True) # перестраивает элементы списка в обратном порядке по убыванию
# print(a)

# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len)  # сортировка по длине символов
# print(b)
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3, ]
# print(a)
# # a.sort()
# # print(a)
# sort = sorted(a, reverse=True)  # функция для сортировки
# print(sort)
# print(a)

# Генерация случайных данных

import random

# print(random.random())
# print(random.randint(3, 9))  # (3, 9) - от 3 по 9 (включительно)
# print(random.randrange(3, 9, 2))  # (3, 9) - от 3 по 9 (не включительно)
#
# print(round(random.uniform(10.5, 25.5), 2))  # вещественное число с заданным количеством после точки
#
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list))  # выбрали одно какое-то значение из списка
# print(random.choices(city_list, k=3))  # возвращает случайное заданное количество элементов из списка
# random.shuffle(city_list)  # перемешали элементы случайным образом
# print(city_list)

# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 3, 21, 1]
# # print(random.choice(s))
# print(random.choices(s, k=5))

# lst = [5, 4, 3, 2, 1]
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))

# lst = ["5", "4", "3", "2", "1"]
# print(len(lst))
# # print(sum(lst))  # не работает с типом данных str
# print(min(lst))
# print(max(lst))

# a = [5, 4, 3, 2, 1]
# res = 0
# for i in a:
#     res += i
# print(res)
# print(sum(a))

# a = 5
# print(a)
# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 3, 21, 1]
# print(sum(s))

import random

# mas = [i for i in range(10)]
# print(mas)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mas = [random.randint(0, 20) for i in range(10)]
# print(mas)

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# a = max(lst)
# print("Max: ", a)
# lst.remove(a)
# lst.insert(0, a)
# print(lst)

# import random
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# min_ch = min(lst)
# print("Min: ", min_ch)
# ind = lst.index(min_ch)
# print("Index min: ", ind)
# print(lst[ind:])
# #  или
# # del lst[0: ind]
# # print(lst)

# x = list("1a2b3c4d")
# print(x)
# print("a" in x)
# print("e" in x)
# print("a" not in x)
# print("e" not in x)

# lst = []
# if len(lst) == 0:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")

# lst = []
# print(bool(lst))
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")


# import random
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print("Третий список:", c)
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in d:
#         d.append(element)
# print("Элементы списков без повторений:", d)
# o = []
# for element in a:
#     if element in b and element not in o:
#         o.append(element)
# print("Элементы общие для двух списков:", o)
# f = [min(a), min(b), max(a), max(b)]
# print("Минимальное и максимальное значение каждого из списков:", f)


# HomeWork
# import random
# n1 = int(input("Размер списка: "))
# a = [random.randint(0, n1-1) for i in range(n1)]
# s = []
# for i in range(len(a)):
#     if i not in a:
#         a.append(i)
# for i in a:
#     if i not in s:
#         s.append(i)
# print("Уникальные случайные числа:", s)

#
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # m = ["Hello", "World"]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 4, 3
# # matrix = [[0 for x in range(w)]for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

import random

# w, h = 4, 3
# matrix = [[random.randint(1, 30) for x in range(w)]for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# import random
# w, h = 3, 4
# matrix = [[random.randint(-20, 10) for i in range(w)] for j in range(h)]
# count = 0
# for row in matrix:
#     for i in row:
#         print(i, end="\t")
#         if i < 0:
#             count += 1
#     print()
# print("Количество отрицательных элементов: ", count)

# for x, y, z in [[1, 2, 6], [3, 4, 8], [5, 6, 2], [7, 8, 4]]:
#     print(x, "+", y, "=", x + y)

# import random
# w, h = 4, 3
# matrix = [[int(input("Введите число: ")) for x in range(w)]for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# import math
# num1 = math.sqrt(4)
# num2 = math.ceil(3.1)
# num3 = math.floor(3.8)
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)

# import math as m  # даем псевдоним модулю
# num1 = m.sqrt(4)
# print(num1)

# import math as m
# from math import sqrt, ceil
# num1 = sqrt(4)
# num2 = ceil(3.1)
# print(num1)
# print(num2)

# from math import *
# num1 = sqrt(4)
# print(num1)

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru") # дату и время переводим на русский язык

# seconds = time.time()
# print("Количество секунд:", seconds)
# local_time = time.ctime(1407662899)
# print("Местное время:", local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
# # print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()))
# print(time.strftime("Сегодня: %B %d, %Y"))

# start = time.time()
# time.sleep(5)  # задержка программы на 5 секунд
# finish = time.time()
# res = finish - start
# print(res)

# start = time.monotonic()
# time.sleep(5)  # задержка программы на 5 секунд
# finish = time.monotonic()
# res = finish - start
# print(res)


#    Function
# print()
#
#
# def hello(name):  # аргументы
#     print("Hello,", name)
#
#
# hello("Igor")  # параметры
# hello("Irina")  # параметры

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', 'O')


# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res * 2)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))


# def res(one, two):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print('Результат: ', res(a, b))


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# def change(lst):
#     symbol1 = lst.pop(0)
#     symbol2 = lst.pop()
#     lst.append(symbol1)
#     lst.insert(0, symbol2)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['H', 'e', 'l', 'l', 'o']))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['H', 'e', 'l', 'l', 'o']))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 20
# b = 15
# print(is_greater(a, b))
# print(is_greater(10, 5))
#
# if is_greater(a, b):
#     print(a, 'больше', b)
# else:
#     print(b, 'больше', a)


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# HomeWork
# import math
#
#
# def check_rectangle(rec):
#     if check_shape == 1:
#         w = int(input("Введите ширину: "))
#         h = int(input("Введите высоту: "))
#         return w * h
#
#
# def check_triangle(a):
#     if check_shape == 2:
#         o = int(input("Введите основание: "))
#         c = int(input("Введите сторону: "))
#         return (o * c) / 2
#
#
# def check_circle(r):
#     if check_shape == 3:
#         r = int(input("Введите радиус: "))
#         return r * math.pi
#
#
# rectangle = 1
# triangle = 2
# circle = 3
# check_shape = int(input("Выберите фигуру: 1 - прямоугольник, 2 - треугольник, 3 - круг: "))
#
# if check_shape == 1:
#     print("Площадь прямоугольника: ", check_rectangle(1))
# if check_shape == 2:
#     print("Площадь треугольника: ", check_triangle(2))
# if check_shape == 3:
#     print("Площадь круга: ", check_circle(3))


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# n1 = 1
# n2 = 5
# n4 = 2
# print(get_sum(n1, n2, d=n4))


# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, "*")
# set_param(s="$")


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         if not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print("Сумма четных чисел: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных чисел: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
#
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
# print(a == b)  # True
# print(a is b)  # True
#
# n = 5
# m = 5
# print(id(n))
# print(id(m))
# print(n == m)  # True
# print(n is m)  # True

# n = "Hello"
# print(id(n))
# n = "Python"
# print(id(n))

# n = [1, 2, 3]
# print(id(n))
# n.append(4)
# print(n)
# print(id(n))


# Картеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())  # Размер в операционной системе
# print(tpl.__sizeof__())

# a = (5,)
# print(type(a))
# print(a)
#
# n = ["Hello", "Python"]
# b = tuple(n)
# print(type(b))
# print(b)

# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3])  # 4
# print(a[1:3])  # (2, 3)
# # a[1] = 3  # не работает  TypeError

from random import randint

# s = tuple(int(input("-> ")) for i in range(5))
# s = tuple(randint(0, 100) for i in range(5))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("Hello")
# t2 = tuple("World")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# print(t3.count('l'))
# print(t1 * 2)

# if "e" in t3:
#     print(t3.index("e"))

# for i in t3:
#     print(i, end="")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # a = tpl.index(el)
#             # b = tpl.index(el, a + 1)
#             # return tpl[a:b + 1]
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['Hello', 'world'])
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# print(x, y, z)

# t = (1, 2, 3)
# x, y, z = t  # распаковка кортежа
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# first_name, year, married = user
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# print(first_name, year, married)
#
# first_name, year, married = get_user()
# print(first_name, year, married)


# #  HomeWork
# from random import randint
# tpl1 = tuple(randint(0, 5) for i in range(10))
# print(tpl1)
# tpl2 = tuple(randint(-5, 0) for x in range(10))
# print(tpl2)
# tpl3 = tuple(tpl1 + tpl2)
# print(tpl3)
# print("0 =", tpl3.count(0))


# from random import randint
#
#
# def create_tuple(start, end):
#     return tuple(randint(start, end) for _ in range(10))
#
#
# tpl1 = create_tuple(0, 5)
# tpl2 = create_tuple(-5, 0)
# tpl3 = tpl1 + tpl2
#
# print(tpl1, tpl2, tpl3, '0 = ' + str(tpl3.count(0)), sep='\n')

# tpl = (1, 2, 3, 4, 5, 6)
# print(tpl)
# lst = list(tpl)
# print(lst)
# ptl1 = tuple(lst)
# print(ptl1)
# del ptl1
# print(ptl1)

# countries = (
#     ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
#     ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население =", city_population)

