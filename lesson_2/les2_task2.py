# https://drive.google.com/file/d/1MNCAi6OvugOI1zHhkWJdEJB3L7W3ljyB/view?usp=sharing
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введи число: \n')
even = 0
odd = 0
for i in num:
    if int(i) % 2:
        odd += 1
    else:
        even += 1
print(f'В числе {num} четных цифр: {even}, нечетных цифр: {odd}')