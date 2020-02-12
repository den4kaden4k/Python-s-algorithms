# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

begin = 1
end = 20
length = 10
array1 = [random.randint(begin, end) for _ in range(length)]
min = array1[0]
max = array1[0]
index_min = 0
index_max = 0
print(array1)
for idx, i in enumerate(array1):
    if i < min:
        min = i
        index_min = idx
    if i > max:
        max = i
        index_max = idx
array1[index_min], array1[index_max] = array1[index_max], array1[index_min]
print(array1)
