
# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
# вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import timeit

def sieve(n):
    fix = [25, 168, 1229, 9592, 78498, 664759]   # константы пи функции, соответствующие 10**2, 10**3, 10**4 и т.д.
    for idx, i in enumerate(fix, start=2):
        if i >= n:
            fix = 10**idx + 1
            break
    array = list(range(fix))
    array[1] = 0
    for i in range(2, fix):
        if array[i]:
            for k in range(2 * i, fix, i):
                array[k] = 0
    out = [m for m in array if m != 0]
    return out[n - 1]

def prime(n):
    num = 3              # начальное число для проверки
    i = 2                # делитель
    k = 1                # счетчик простых чисел
    out = 3
    if n == 1:
        return 2
    while k != n:
        if num % i == 0:
            num += 2
            i = 3
        elif i**2 > num:
            k += 1
            out = num
            num += 2
            i = 3
        else:
            i += 1
    return out

s1 = '''
def sieve(n):
    fix = [25, 168, 1229, 9592, 78498, 664759]   # константы пи функции, соответствующие 10**2, 10**3, 10**4 и т.д.
    for idx, i in enumerate(fix, start=2):
        if i >= n:
            fix = 10**idx + 1
            break
    array = list(range(fix))
    array[1] = 0
    for i in range(2, fix):
        if array[i]:
            for k in range(2 * i, fix, i):
                array[k] = 0
    out = [m for m in array if m != 0]
    return out[n - 1]
    
sieve(1600)
'''
s2 = '''
def prime(n):
    num = 3              # начальное число для проверки
    i = 2                # делитель
    k = 1                # счетчик простых чисел
    out = 3
    if n == 1:
        return 2
    while k != n:
        if num % i == 0:
            num += 2
            i = 3
        elif i**2 > num:
            k += 1
            out = num
            num += 2
            i = 3
        else:
            i += 1
    return out
    
prime(1600)
'''

# 0.0215110   sieve(100)
# 0.0605483   prime(100)
# 0.2251065   sieve(200)
# 0.1876193   prime(200)
# 0.1971800   sieve(400)
# 0.7088207   prime(400)
# 0.1980012   sieve(800)
# 3.3887472   prime(800)
# 3.9595203   sieve(1600)
# 9.7771027   prime(1600)

# print(timeit.timeit(s1, number=100))
# print(timeit.timeit(s2, number=100))
# print(prime(100))
# print(sieve(100))
# Скорость выполнения функции prime(n) при увеличении n в два раза растет линейно, а sieve(n) либо изменяется не значительно,
# либо резко возрастает. В большинстве случаев время выполнения sieve(n) в несколько раз быстрее,
# поэтому я считаю этот алгоритм более эффективным.