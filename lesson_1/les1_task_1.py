
# https://drive.google.com/file/d/16kQgkuy-NSdIt5TXjR9dO3mgPB0liuoL/view?usp=sharing

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input("Введите трехзначное целое число:\n"))
num1 = a % 10
num2 = (a // 10) % 10
num3 = (a // 100) % 10
summa = num1 + num2 + num3
multi = num1 * num2 * num3
print(f'Сумма цифр числа {a} = {summa},\nПроизведение цифр числа {a} = {multi}')