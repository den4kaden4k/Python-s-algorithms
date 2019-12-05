
# https://drive.google.com/file/d/16kQgkuy-NSdIt5TXjR9dO3mgPB0liuoL/view?usp=sharing

# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print('Введи две буквы')
char1 = input('Введи первую букву:\n')
char2 = input('Введи вторую букву:\n')
correction = 96
position1 = ord(char1) - correction
position2 = ord(char2) - correction
range_char = abs((position1 - position2)) - 1
print(f"{char1} находится на позиции {position1}\n{char2} находится на позиции {position2}\n\
Между буквами находится {range_char} букв")