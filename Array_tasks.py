# # Задача 1.Найти площадь и периметр прямоугольного треугольника по двум заданным катетам.
# import math
#
# a = input("Длина первого катета: ")
# b = input("Длина второго катета: ")
#
# a = float(a)
# b = float(b)
#
# c = math.sqrt(a**2 + b**2)
#
# s = (a*b)/2
# p = a + b + c
# #
# print("Площадь треугольника:" + str(s))
# print("Периметр треугольника:"+ str(p))
#
# # Задача2. Найти максимальное число из трех
# # Вводятся три целых числа. Определить какое из них наибольшее.
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# m = int(input("Введите третье число: "))
#
# n = a
# if n < b:
#     n = b
# if n < m:
#     n = m
# print("Наибольшее число:", n)
#
# # Задача 3.Найти площадь прямоугольника, треугольника или круга
# # В зависимости от того, что выберет пользователь, вычислить площадь либо прямоугольника, либо треугольника, либо круга.
# # Если выбраны прямоугольник или треугольник, то надо запросить длины сторон, если круг, то его радиус.
# import math
# choiсe = input("Сделайте выбор: 1 - прямоугольник, 2 - треугольник , 3 - круг - ")
# if choiсe == '1':
#     a = int(input("Введите длину стороны a: "))
#     b = int(input("Введите длину стороны b: "))
#     print("Площадь прямоугольника равна", a*b)
#
# elif choiсe == '2':
#    c = int(input("Введите длину одного катета: "))
#    d = int(input("Введите длину второго катета: "))
#    g = int(input("Введите длину гипотенузы: "))
#    p = (c + d + g)/2
#    print("Площадь треугольника равна", math.sqrt(p * (p-c) * (p-d) * (p-g)))
#
# elif choiсe == '3':
#    r = int(input("Введите длину радиуса: "))
#    print("Площадь круга равна", (math.pi * r ** 2))
#
# else:
#     print("Ошибка")
#
# # Задача 4.Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# # Учитывать только английские буквы. строка : "Hello WOOrld"
# lowercase = 0
# uppercase = 0
# str = "Hello WOOrld"
# for i in str:
#     if 'a' <= i <= 'z':
#         lowercase += 1
#     else:
#         if 'A' <= i <= 'Z':
#          uppercase += 1
#
# print("Количество строчных: ", lowercase)
# print("Количество прописных: ", uppercase)

'''http://www.itmathrepetitor.ru/prog/zadachi-na-massivy-2/'''
# 1.Заполнить массив нулями, кроме первого и последнего элементов, которые должны быть равны единице.
# a=[0 for _ in range(10)]
# a[0] = 1
# a[len(a)-1] = 1
# print(a)

# 2.Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.

# x = int(input("Введите число элементов массива x: "))#Первый способ
# b = []
# for i in range (0,x):
#     if i % 2 == 0:
#         a = 0
#     else:
#         a = 1
#     b.append(a)
# print(b)

# L = [0,1]*10 # Второй способ
# print(L)


# 3.Заполнить массив последовательными нечетными числами, начиная с единицы.
# L = []
# x = int(input("Введите число элементов массива x: "))
# for i in range (1,x):
#     if i % 2 == 1:
#         L.append(i)
# print(L)

# 4.Сформировать массив из элементов арифметической прогрессии с заданным первым элементом x и разностью d.

# x = int(input('Задайте первый элемент массива x: '))
# d = int(input('Введите разность арифметической прогрессии  d: '))
# n = int(input('Введите количество элементов в массиве n: '))
# L = [x + i * d for i in range(0, n)]
# print(L)

# 5.Сформировать возрастающий массив из четных чисел.
# L = []
# L.append(int(input('Введите число: ')))
# L.append(int(input('Введите число: ')))
# L.append(int(input('Введите число: ')))
# L.append(int(input('Введите число: ')))
# L.sort()
# print(L)

# 6.Сформировать убывающий массив из чисел, которые делятся на 3.
# L = []
# x = int(input("Введите величину диапазона: "))
# for i in range(0, x):
#     if i % 3 == 0:
#         L.append(i)
#         L.sort()
#         L.reverse()
# print(L)

# 7.Создать массив из n первых чисел Фибоначчи.
# n = int(input('Введите количество первых чисел Фибоначчи n: '))
# L = []
# def fib_to(n):
#     L = [0, 1]
#     for i in range(2, n):
#         L.append(L[-1] + L[-2])
#     print(L)
#     return L
# fib_to(n)

# 8.Заполнить массив заданной длины различными простыми числами. Натуральное число, большее единицы,
# называется простым, если оно делится только на себя и на единицу
# L = []
# n = int(input('Введите длину рассматриваемого диапазона: '))
# for i in range(2,n+1):
#     count = 0
#     for j in range(2,i):
#         if i%j != 0:
#             count += 1
#     if count == i-2:
#         L.append(i)
#
# print(L)


# 9.Создать массив, каждый элемент которого равен квадрату своего номера.
# m = int(input('Введите число, с которого начнутся вычисления: '))
# n = int(input('Введите последнее число для вычислений: '))
# L = []
# for i in range(m, n+1):
#     a = i**2
#     L.append(a)

# print(L)

# 10. Создать массив, на четных местах в котором стоят единицы, а на нечетных местах - числа, равные
# остатку от деления своего номера на 5. #
# n = int(input('Введите длину массива: '))
# L = []
# for i in range(n):
#     if i % 2 == 0:
#         a = 1
#     else:
#         a = i % 5
#         print (i % 5)
#     L.append(a)
#
# print(L)