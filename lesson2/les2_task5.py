
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def convert_num_to_symbol(start, stop, num):
    count = num
    for i in range(start, stop + 1):
        print(f'[{i} - {chr(i)}] ', end='')
        if (i - start + 1) == count:
            count += num
            print()


convert_num_to_symbol(32, 127, 10)
