
# https://drive.google.com/file/d/16kQgkuy-NSdIt5TXjR9dO3mgPB0liuoL/view?usp=sharing

# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введи три разных целых числа:')
a = input('Первое число\n')
b = input('Второе число\n')
c = input('Третье число\n')
if b < a < c or b > a > c:
    print(f'Число {a} среднее')
    quit()
if a < b < c or a > b > c:
    print(f'Число {b} среднее')
    quit()
else:
    print(f'Число {c} среднее')