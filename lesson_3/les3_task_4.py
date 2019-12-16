# Определить, какое число в массиве встречается чаще всего.

import random

begin = 1
end = 11
length = 20
array = [random.randint(begin, end) for _ in range(length)]
unique_num = set(array)
count_max = 0
num_max = 0
for i in unique_num:
    count = 0
    for num in array:
        if num == i:
            count += 1
    if count > count_max:
        count_max = count
        num_max = i
print(f'В массиве {array}')
print(f'Число {num_max} встречается чаще всего, {count_max} раз')



