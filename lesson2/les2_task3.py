# https://drive.google.com/file/d/1MNCAi6OvugOI1zHhkWJdEJB3L7W3ljyB/view?usp=sharing
# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = input("Введи число: \n")
reverse = ''
i = 0
while i != len(num):
    reverse += num[-1 - i]
    i += 1
print(f'Число {num} в обратном порядке: {reverse}')
