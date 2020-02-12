# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

from collections import Counter
import sys


def show_size(*x):
    cnt = 0
    for k in x:
        if hasattr(k, '__iter__') and not isinstance(k, type):
            if hasattr(k, 'items'):
                for key, value in k.items():
                    cnt += sys.getsizeof(key) + sys.getsizeof(value)
            elif not isinstance(k, str):
                for itm in k:
                    cnt += sys.getsizeof(itm)
        else:
            cnt += sys.getsizeof(k)
    print(f'size = {cnt}')


# Вариант кода №1

def count(number, digit):
    cnt = list(str(number)).count(str(digit))
    print('Функция count():', end=' ')
    show_size(cnt, number, digit, list(str(number)), str(number), str(digit))
    return cnt


# Вариант кода №2


def count2(number, digit):
    digits = Counter(str(number))
    num = digits[str(digit)]
    print('Функция count2():', end=' ')
    show_size(number, digit, digits, str(number), str(digit), num)
    return num


# Вариант кода №3

def count3(x, y):
    number = x
    digit = y
    cnt = 0
    while number:
        num = number % 10
        if num == digit:
            cnt += 1
        number //= 10
    print('Функция count3():', end=' ')
    show_size(cnt, x, y)
    return cnt


count_num = int(input('Сколько чисел будешь вводить?\n'))
numbers = []
for i in range(1, count_num + 1):
    num = input(f'Введи число {i}\n')
    numbers.append(num)
b = int(input('Какую цифру посчитать? \n'))
a = 0
for itm in numbers:
    a += count(int(itm), b)
print('Total', end=' ')
show_size(count_num, numbers, count_num + 1, numbers[-1], b, a)
print(f'{b} встретилась {a} раз')


# Для всех трех функций использовались следующие тестовые значения переменных: count_num = 1, num = 1234512345, b = 2
# Размер участка кода общего для всех функций Total size = 171 байт
# Размер функции count() = 588
# Размер функции count2() = 478
# Размер функции count3() = 88
# Оптимальной по размеру занимаемой памяти оказалась функция count3(), т.к. в ней использовались только числовые значения переменных.

