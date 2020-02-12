# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        middle = len(array) // 2
        return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i != len(left):
        result.append(left[i])
        i += 1
    while j != len(right):
        result.append(right[j])
        j += 1
    return result


arr = [round((random.random() * 49), 1) for _ in range(10)]
print(arr)
print(merge_sort(arr))
