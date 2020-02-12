# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

dec_to_hex = {}
hex_to_dec = {}
for i in range(16):
    dec_to_hex[i] = hex(i)[-1].upper()
    hex_to_dec[hex(i)[-1].upper()] = i


def total(*args):
    numbers = deque()
    for i in args:
        if type(i) is deque:
            numbers.append(i)
        else:
            for item in i:
                numbers.append(item)
            break
    temp_num1 = deque(numbers[0])
    temp_num2 = deque(numbers[1])
    temp_sum = deque()
    for k in range(2, len(numbers) + 1):
        dif = len(temp_num1) - len(temp_num2)
        if dif > 0:
            temp_num2.extendleft('0' * dif)
        if dif < 0:
            temp_num1.extendleft('0' * abs(dif))
        tail = 0
        for n in range(-1, -len(temp_num1) - 1, -1):
            sum = hex_to_dec[temp_num1[n]] + hex_to_dec[temp_num2[n]] + tail
            if sum < 16:
                temp_sum.extendleft(dec_to_hex[sum])
                tail = 0
            else:
                temp_sum.extendleft(dec_to_hex[sum % 16])
                tail = sum // 16
        if tail:
            temp_sum.extendleft('1')
        if k == len(numbers):
            break
        temp_num1 = temp_sum
        temp_num2 = numbers[k]
        temp_sum = deque()
    return list(temp_sum)


def multi(a, b):
    multi_temp = deque()
    multi_list = []
    tail = 0
    f = '0'
    for m in range(-1, -len(a) - 1, -1):
        for num in range(-1, -len(b) - 1, -1):
            multi1 = hex_to_dec[a[m]] * hex_to_dec[b[num]] + tail
            if multi1 < 16:
                multi_temp.extendleft(dec_to_hex[multi1])
                tail = 0
            else:
                multi_temp.extendleft(dec_to_hex[multi1 % 16])
                tail = multi1 // 16
        if tail:
            multi_temp.extendleft(dec_to_hex[tail])
            tail = 0
        if len(multi_list) > 0:
            multi_temp.extend(f)
            f += '0'
        multi_list.append(multi_temp)
        multi_temp = deque()
    if len(multi_list) < 2:
        return list(multi_list)
    return list(total(multi_list))


hex1 = deque(input('Введите первое шестнадцатеричное число:\n').upper())
hex2 = deque(input('Введите второе шестнадцатеричное число:\n').upper())

print(f'Сумма чисел = {total(hex1, hex2)}')
print(f'Произведение чисел = {multi(hex1, hex2)}')

