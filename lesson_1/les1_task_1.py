
# https://drive.google.com/file/d/16kQgkuy-NSdIt5TXjR9dO3mgPB0liuoL/view?usp=sharing

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input("Введите трехзначное целое число:\n"))
num1 = a % 10
num2 = int(a / 10)
num3 = int(num2 / 10)
summa = num1 + num2 % 10 + num3 % 10
multi = num1 * (num2 % 10) * (num3 % 10)
print(f'Сумма цифр числа {a} = {summa},\nПроизведение цифр числа {a} = {multi}')