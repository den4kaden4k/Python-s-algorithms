
# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.

# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…

import timeit
import cProfile

def function1(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return -1 / 2 ** (n - 1) + function1(n - 1)
    else:
        return 1 / 2 ** (n - 1) + function1(n - 1)


def function2(n):
    temp = 0
    for i in range(n):
        if i % 2 == 0:
            temp = 1 / 2 ** i + temp
        else:
            temp = -1 / 2 ** i + temp
    return temp


def function3(n):
    return sum(map(lambda x: -1 / 2 ** x if x % 2 != 0 else 1 / 2 ** x, range(n)))

s1 = '''
def function1(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return -1 / 2 ** (n - 1) + function1(n - 1)
    else:
        return 1 / 2 ** (n - 1) + function1(n - 1)
        
function1(400)
'''
s2 = '''
def function2(n):
    temp = 0
    for i in range(n):
        if i % 2 == 0:
            temp = 1 / 2 ** i + temp
        else:
            temp = -1 / 2 ** i + temp
    return temp
    
function2(400)
'''
s3 = '''
def function3(n):
    return sum(map(lambda x: -1 / 2 ** x if x % 2 != 0 else 1 / 2 ** x, range(n)))
    
function3(400)
'''
# 0.008126599999999998    function1(100)
# 0.006158799999999999    function2(100)
# 0.006252599999999997    function3(100)

# 0.019863799999999997    function1(200)
# 0.013345999999999997    function2(200)
# 0.014151700000000003    function3(200)

# 0.038417599999999996    function1(400)
# 0.029433100000000004    function2(400)
# 0.03094200000000001     function3(400)
cProfile.run('function1(400)')
# 100/1    0.000    0.000    0.000    0.000 les4_task_1.py:7(function1)  function1(100)
# 200/1    0.000    0.000    0.000    0.000 les4_task_1.py:7(function1)  function1(200)
# 400/1    0.002    0.000    0.002    0.002 les4_task_1.py:7(function1)  function1(400)

# print(timeit.timeit(s1, number=100))
# print(timeit.timeit(s2, number=100))
# print(timeit.timeit(s3, number=100))
# Вывод: Оценка времени выполнения всех трех функций при увеличении n в два раза демонстрирует линейную зависимость.
# Функции function2(n) и function3(n) выполняются примерно за одинаковое время, поэтому их реализации я считаю оптимальными.