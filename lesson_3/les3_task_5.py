# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

begin = -99
end = 11
length = 30
array = [random.randint(begin, end) for _ in range(length)]
min_ = 0
pos = 0
for idx, i in enumerate(array):
    if i < min_:
        min_ = i
        pos = idx
print(f'В массиве: {array}')
print(f'Отрицательный элемент отсутствует' if min_ == 0 else f'Минимальный элемент {min_} находится на позиции {pos}')
