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

# 11.Создать массив, состоящий из троек подряд идущих одинаковых элементов.
# L = [f * 3 for f in 'Minsk']
# print(L)


# # 12.Создать массив, который одинаково читается как слева направо, так и справа налево.
# import random
# L = [random.randint(0 ,9) for x in range(random.randint(10,10))]# создаю массив
# print(L)
# print(len(L))
#
# halfL = 0
# if len(L) % 2 == 1: # нахожу половину массива, при нечетной его длине
#     halfL = (len(L)-1) /2
# else:
#     halfL = len(L) / 2 # половина массива при четной длине
#
# print(halfL)
# for i in range(int(halfL)): # до конца половины массива
#     L[len(L) - 1 - i] = L[i] # перезаписываю последний элемент массива по порядку, начиная с первого
#
# print(L)

#13.Сформировать массив из случайных чисел, в которых ровно две единицы, стоящие на случайных позициях.
# import random
# L = [random.randint(1, 2) for x in range(5)]
# print(L)
# while L.count(1) > 2:
#     L.remove(1)
#
# while L.count(1) < 2:
#     L.append(1)
# print(L)

# 14.Заполните массив случайным образом нулями и единицами так, чтобы количество единиц было больше количества нулей.
# import random
# L = [random.randint(0,1) for x in range(6)]
# if L.count(1) <= L.count(0):
#     M = [1]*L.count(0)
#     L = L + M
# print(L)

# 15.Сформировать массив из случайных целых чисел от 0 до 9 , в котором единиц от 3 до 5 и двоек больше троек.
# import random

# L = [random.randint(0,9) for x in range(10)]
# print(L)
# while L.count(1) > 5:
#     L.remove(1)
# while L.count(1) < 3:
#     L.append(1)
# while L.count(2) <= L.count(3):
#     L.append(2)
# print(L)

# 16.Создайте массив, в котором количество отрицательных чисел равно количеству положительных и положительные
# числа расположены на случайных местах в массиве.

# import random
# L = [random.randint(0, 10) for x in range(5)]
# print(L)
#
# even = 0
# odd = 0
# for i in L:
#     if i % 2 == 0:
#         even+=1
#     else:
#         odd+=1
#
# while even > odd:
#     L.append(1)
#     odd+=1
# while odd > even:
#     L.append(2)
#     even +=1
# print(L)

# 17.Заполните массив случайным образом нулями, единицами и двойками так, чтобы первая двойка в массиве
# встречалась раньше первой единицы, количество единиц было в точности равно суммарному количеству нулей и двоек.
# import random
#
# L = [random.randint(0, 2) for _ in range(9)]
# print(L)
#
# if L.index(2) > L.index(1):
#     L[L.index(1)] = 0
# print(L)
#
# sum02 = L.count(0) + L.count(2)
# print(sum02)
#
# while L.count(1) < sum02:
#     L.append(1)
# while L.count(1) > sum02:
#     L[L.index(1)] = 0
# print(L)


# 18.Придумайте правило генерации массива заданной длины. Определите, сгенерирован ли данный массив вашим правилом или нет.
# import random
# num = int(input('Введите длину массива: '))
# L = [random.randint(0, 15) for _ in range(num)]
# print(L)
# for i in L:
#     if i % 2 == 1:
#        L.append(1000)
# print(L)

# L1 = [x + y for x in 'sunny' if x != 'n' for y in 'run' if y != 'u']# генератор списка 2
# print(L1)

# 19.Определить, содержит ли массив данное число x
# import random

# L = [random.randint(0, 15) for _ in range(10)]
# print(L)
# x = int(input('Введите число: '))
# if x in L:
#     print(x)

# 20.Найти количество четных чисел в массиве.
# L = [1,2,3,4,5,6,7,8,9]
# count = 0
# for i in L:
#     if i % 2 == 0:
#         count += 1
# print(count)


# 21.Найти количество чисел в массиве, которые делятся на 3, но не делятся на 7.
# import random
# L = [random.randint(1, 19) for _ in range(10)]
# print(L)
# count = 0
# for i in L:
#     if i % 3 == 0 and i % 7 != 0:
#         count += 1
# print(count)

# 22.Определите, каких чисел в массиве больше: которые делятся на первый элемент массива
# или которые делятся на последний элемент массива.
# import random
# L = [random.randint(1, 9) for _ in range(5)]
# print(L)
# countX = 0
# countY = 0
# for i in L:
#     if i % L[0] == 0:
#         countX += 1
#     if i % L[-1] == 0:
#         countY += 1
# if countX > countY:
#     print('Чисел, делящихся на перавый элемент массива больше')
# elif countY == countX:
#     print('Одинаковое количество')
# else:
#     print('Чисел, делящихся на последний элемент массива больше')
# print(countX)
# print(countY)

# 23.Найдите сумму и произведение элементов массива.
# import random
# L = [random.randint(1, 9) for _ in range(5)]
# print(L)
# m = 1
# for i in L:
#     m *= i
# print('Произведение элементов массива равно: ', m)
# print('Сумма элементов массива равна: ', sum(L))

# 24.Найдите сумму четных чисел массива.
# import random
# L = [random.randint(1, 9) for _ in range(5)]
# print(L)
# M = []
# for i in L:
#     if i % 2 ==0:
#         M.append(i)
# print(sum(M))

# 25.Найдите сумму нечетных чисел массива, которые не превосходят 11.
# import random
# L = [random.randint(1, 20) for _ in range(5)]
# print(L)
# M = []
# for i in L:
#     if i % 2 == 1 and i <= 11:
#         M.append(i)
# print(M)
# print(sum(M))

# 26.Найдите сумму чисел массива, которые расположены до первого четного числа массива. Если четных
# чисел в массиве нет, то найти сумму всех чисел за исключением крайних.
# import random
# L = [random.randint(1, 6) for _ in range(5)]
# print(L)
# sum1 = 0
# isEven = False
# for i in L:
#     if i % 2 == 1:
#         sum1 += i
#     else:
#         isEven = True
#         break
# if isEven == False:
#     print('sum(L[1:-1]): ', sum(L[1:-1]))
# else:
#     print('sum1 :', sum1)

# 27.Найдите сумму чисел массива, которые стоят на четных местах.
# import random
# L = [random.randint(0, 9) for _ in range(6)]
# print(L)
# print(L[1::2])
# M = []
# M.append(sum(L[1::2]))
# print(M)

# 28.Найдите сумму чисел массива, которые стоят на нечетных местах и при этом превосходят сумму крайних элементов массива.
# import random
# L = [random.randint(0, 9) for _ in range(9)]
# print(L)
# M = L[0::2]
# N = L[0::2]
# print('M:', M)
# print('N:', N)
# summ = L[0] + L[-1]
# print(summ)
# c = [a + b for a in M[1:] for b in N[:-1]]
#
# print('maxc: ', max(c))
# if max(c) > summ:
#     print('Искомая сумма чисел: ', max(c))
# else:
#     print('Нет такой суммы')

# 29.Дан массив x из n элементов. Найдите x1−x2+x3−…−xn−1+xn.
# import random
# x = [random.randint(1, 5) for _ in range(5)]
# print(x)
# sum1 = 0
# a = 1
# for i in x:
#     sum1 = sum1 + i*a
#     a = a * (-1)
# print(sum1)

# 30.Дан массив x из n элементов. Найдите x1xn+x2xn−1+…+xnx1.
# import random
# n = int(input('Введите количество элементов в массиве: '))
# x = [random.randint(1, 3) for _ in range(n)]
# print('x:', x)
# y = x[::-1]
# print('y:', y)
# i = 0
# c = []
# while i < len(x):
#     c.append(x[i]*y[i])
#     i += 1
# print(c)
#
# if n % 2 == 1:
#     f = int((len(x) - 1) / 2)
#     print('x[f]: ', x[f])
#     print('sumC: ', sum(c))
#     sumOddn = x[f] * x[f] + 2 * (sum(c) - x[f] * x[f])
#     print('Сумма при  нечетном n равна: ', sumOddn)
# else:
#     sumEventn = 2 * (sum(c))
#     print('Сумма при четном n равна: ', sumEventn)

# 31.Дан массив x из n элементов. Найдите xn(xn+xn−1)(xn+xn−1+xn−2)…(xn+…+x1).
# import random
# n = int(input('Введите количество элементов в массиве: '))
# L = [random.randint(1, 3) for _ in range(n)]
# print(L)
# print(L[-1:])
# indSum = len(L)-1
#
# res = 1
# sum = 0
#
# while indSum >= 0:
#     for i in L[indSum:]:
#         sum += i
#     print('sum:', sum)
#     indSum = indSum - 1
#     res *= sum
#     print(res)
#     sum = 0
# print('res:', res)

# 32.Найти наибольший элемент массива.
# import random
# L = [random.randint(0, 9) for _ in range(6)]
# print(L)
# print(max(L))

# 33.Найдите сумму наибольшего и наименьшего элементов массива.
# import random
# L = [random.randint(0, 9) for _ in range(6)]
# print(L)
# y = max(L)
# x = min(L)
# b = x + y
# print('Сумма наибольшего и наименьшего элементов равна: ',b)

# 34.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.
# import random
# L = [random.randint(0, 100) for _ in range(25)]
# print(L)
# y = max(L)
# print(max(L))
# count = 0
# for i in L:
#     if i == y - (y/100)*10:
#         count +=1
# print(count)

# 35.Найдите наименьший четный элемент массива.
# import random
# L = [random.randint(0, 9) for _ in range(6)]
# print(L)
# M = []
# for i in L:
#     if i %2 ==0:
#         M.append(i)
# print(min(M))

# 36.Среди элементов с нечетными номерами найдите наибольший элемент массива, который делится на 3.
# import random
# L = [random.randint(0, 33) for _ in range(6)]
# print(L)
# M = []
# N = []
# for i in L:
#     if i % 2==1:
#         M.append(i)
# for i in M:
#     if i % 3 == 0:
#         N.append(i)
# print(max(N))

# 37.Дан массив и число p. Найдите два различных числа в массиве, сумма которых наиболее близка к p.
# import random
# #
# L = [random.randint(0, 9) for i in range(int(input('Введите размер массива: ')))]
# print(L)
# p = int(input('Введите число: '))
# a = 0
# b = 1
# nearestSum = abs(p - (L[a] + L[b]))
#
# for i in range(len(L)):
#     for j in range(len(L)):
#         if i == j:
#             continue
#         sum = abs(p - (L[i] + L[j]))
#         if sum < nearestSum:
#             nearestSum = sum
#             a = i
#             b = j
#
# print('res1: ', a)
# print('res2: ', b)
# print('a ', L[a], " ", 'b', L[b])

# 38.Дан массив. Найдите два соседних элемента, сумма которых минимальна.
# import random
# L = [random.randint(0, 9) for _ in range(6)]
# print(L)
#
# a = L[0]
# b = L[1]
# pred = L[0]
#
# for i in L[1:]:
#     if (a + b) > (pred + i):
#         a = pred
#         b = i
#     pred = i
#
# print(a)
# print(b)

# 39.Дан массив. Найдите три последовательных элемента в массиве, сумма которых максимальна.
# import random
# L = [random.randint(0, 9) for _ in range(6)]
# print(L)
#
# a = L[0]
# b = L[1]
# c = L[2]
# pred1 = L[0]
# pred2 = L[1]
#
# for i in L[2:]:
#     if (a + b + c) < (pred1 + pred2 + i):
#         a = pred1
#         b = pred2
#         c = i
#     pred1 = pred2
#     pred2 = i
#
# print(a)
# print(b)
# print(c)

# 40.В данном массиве найдите количество чисел, соседи у которых отличаются более чем в 2 раза.
# import random
# L = [random.randint(1, 9) for _ in range(9)]
# print(L)
#
# pred = L[0]
# a = L[1]
#
# count = 0
# for i in L[1:]:
#     if (pred / i) > 2 or (i / pred) > 2:
#         count += 1
#         pred = a
#
# print(count)

# 41.Найдите количество чисел, каждое из которых равно сумме квадратов своих соседей и при этом не является наибольшим в массиве.
# import random
# L = [random.randint(0, 4) for _ in range(15)]
# print(L)
# # L = [ 3, 25, 4, 0, 1,2,1,0,0,0,1,5,2]
# maxL = max(L)
# print('maxL:', maxL)
# count = 0
# pred1 = L[0]
# pred2 = L[1]
#
# for i in L[2:]:
#     if pred2 == (pred1*pred1 + i*i) and pred2 != maxL:
#         count += 1
#     pred1 = pred2
#     pred2 = i
# print(count)

# 42.Проверьте, содержит ли данный массив из n чисел, все числа от 1 до n.

# import random
# n = int(input('Введите количество чисел массива: '))
# L = [random.randint(1, n) for _ in range(n)]
# print(L)
# c = 0
# b = 0
# for i in range(len(L)):
#     for j in range(len(L)):
#         if i == j:
#             continue
#         if L[i] == L[j]:
#             c = 1
#         else:
#             b = 1
# if c == 1:
#     print('no')
# elif b == 1:
#     print('yes')

# 43.Проверьте, образует ли элементы массива в данном порядке арифметическую или геометрическую прогрессии.
# L = [10, 20, 30, 40, 50]
# L = [2, 4, 8, 16]
#
#
# isGeom = True
# denominator = L[1] / L[0]
# pred = L[0]
# for i in L[1:]:
#     if i / pred == denominator:
#         pred = i
#     else:
#         isGeom = False
#         break
# if isGeom:
#     print('Это геометрическая прогрессия')
# else:
#     print('Это не геометическая прогрессия')
#
# isArif = True
# razn = L[1] - L[0]
# pred = L[0]
# for i in L[1:]:
#     if i - pred == razn:
#         pred = i
#     else:
#         isArif = False
#         break
# if isArif:
#     print('Это арифметическая прогрессия')
# else:
#     print('Это не арифметическая прогрессия')



# 44.Проверьте, является ли данный массив возрастающим или убывающим.
# import random
# L = [random.randint(0, 5) for _ in range(5)]
# print(L)
# # L = [1, 2, 3, 4, 5]
# a = L[0]
# b = L[1]
# increases = 0
# decreases = 0
# for i in L:
#     if a < b:
#         increases += 1
#         a = b
#         b = i
#     else:
#         decreases +=1
#         a = b
#         b = i
# if increases > decreases:
#     print('Массив возрастающий')
# else:
#     print('Массив убывающий')

# 45.Найдите количество различных элементов данного массива.
'''вариант1'''
# a = [1,'',3,2,'3',2,2,3,'3',3,'5']
# d = {x:a.count(x) for x in a}
# print(d)
'''вариант2'''
# import collections
# a = [1, '', 3, 2, '3', 2, 2, 3, '3', 3, '5']
# counter = collections.Counter(a)
# print(counter)
# print(f'Элементы: {counter.keys()} в количестве: {counter.values()}')
'''вариант3'''
# a = [1,'',3,2,'3',2,2,3,'3',3,'5']
# b = {}
# for item in a:
#        b[item] = b.get(item, 0) + 1
# print(b)

# 46.Определите количество перемен знаков элементов массива.
# L = [-1, -1, 1, 1, -1, -1, 1, -1, 1]
#
# def count(L):
#     prev = 0
#     res = 0
#     for i in L:
#
#         if prev * i < 0:
#             res += 1
#         else:
#             0
#         if i != 0:
#             prev = i
#         else:
#             prev
#     return res
# print(count(L))
# print (count([-1, 0, 1, -1, 0, 0, 0, 2, 0, -1]))
        # def count(l):# необычная запись решения
        #     prev = 0
        #     r = 0
        #     for value in l:
        #         r += 1 if prev * value < 0 else 0
        #         prev = value if value != 0 else prev
        #     return r
        #
        # print count([-1, 0, 1, -1, 0, 0, 0, 2, 0, -1]) # -> 4

# 47.В данном массиве найти максимальное количество одинаковых элементов.
# a = [1, '', 3, 3, 2, '3', 2, 2, 3, '3', 3, '5', 3]
# d = {x:a.count(x) for x in a}
# print(d)
# print(d.values())
# countEl = d.values()
# print('Максимальное количество: ', max(countEl))

# 48.Найти наиболее часто встречающийся элемент в массиве целых чисел.

# import random
# n = int(input('Введите количество чисел массива: '))
# L = [random.randint(1, n) for _ in range(n)]
# print(L)
# count = 0
# res = 0
# d = {x:L.count(x) for x in L}
# print(d)
#
# for i in L:
#     if L.count(i) > count:
#         count = L.count(i)
#         res = i
# print('Наиболее часто встречающийся элемент в массиве:', res ,'встречается', count , 'раз(а)')

# 49.В одномерном массиве, состоящем из n вещественных элементов, вычислите номер минимального элемента массива и сумму
# элементов массива, расположенных между первым и вторым отрицательными элементами.
# import random
# n = int(input('Введите длину массива: '))
# L = [round(random.uniform(-100, 100), 3) for i in range(n)]
# print(L)
# print('Номер минимального элемента массива:', L.index(min(L))+1)
#
# minus = []
# for i in range(len(L)):
#     if len(minus) == 2:
#         break
#     elif L[i] < 0:
#         minus.append(L[i])
# print('Искомая сумма равна:', sum(L[L.index(minus[0])+1:L.index(minus[1])]))

# 50.Напишите программу, которая вводит с клавиатуры непустой массив целых чисел, и выводит число
# локальных максимумов (элемент является локальным максимумом, если он не имеет соседей, больших, чем он сам).

# L = []
# a = int(input('Введите первое число'))
# b = int(input('Введите второе число'))
# c = int(input('Введите третье число'))
# d = int(input('Введите четвертое число'))
# e = int(input('Введите пятое число'))
# L.append(a)
# L.append(b)
# L.append(c)
# L.append(d)
# L.append(e)
# print(L)
# pred = L[0]
# a = L[1]
# b = L[2]
# count = 0
# for i in L:
#     if a > pred and a > b:
#         count +=1
#         pred = a
#         a = b
#         b= i
#     else:
#         pred = a
#         a = b
#         b = i
# print(count)