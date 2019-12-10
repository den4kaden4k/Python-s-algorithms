# https://drive.google.com/file/d/1MNCAi6OvugOI1zHhkWJdEJB3L7W3ljyB/view?usp=sharing
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

def function(n, m=1):
    if n == m:
        return 1
    elif m < n and m % 2 != 0:
        return -1 / 2**m + function(n, m+1)
    else:
        return 1 / 2**m + function(n, m+1)


a = int(input('Введи количество элементов: \n'))
print(f'Сумма {a} элементов ряда чисел: 1, -0.5, 0.25, -0.125,… = {function(a)}')