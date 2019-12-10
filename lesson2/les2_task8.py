
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def count(number, digit, pos=0):
    if pos == len(number):
        return 0
    if int(number[pos]) == digit:
        return 1 + count(number, digit, pos+1)
    else:
        return count(number, digit, pos+1)

a = input('Введи число: \n')
b = int(input('Какую цифру посчитать? \n'))
print(f'{b} встретилась {count(a, b)} раз в {a}')

