
# https://drive.google.com/file/d/16kQgkuy-NSdIt5TXjR9dO3mgPB0liuoL/view?usp=sharing

# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

char = int(input('Введи номер буквы\n'))
if char > 26:
    print("Это не буква")
    quit()
correction = 96
f_char = chr(char + correction)
print(f_char)