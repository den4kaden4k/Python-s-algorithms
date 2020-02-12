# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

table = defaultdict(list)
count = int(input('Введите количество предприятий: \n'))
for i in range(count):
    name = input(f'Введите наименование предприятия №{i + 1}\n')
    for q in range(1, 5):
        earn = int(input(f'Введите прибыль за {q} - й квартал\n'))
        table[name].append(earn)
medium_earn = 0
for key in table:
    medium_earn += sum(table[key]) / 2
print(f'Средняя прибыль за год всех предприятий: {medium_earn}')
for key in table:
    if sum(table[key]) >= medium_earn:
        print(f'Прибыль предприятия {key} - выше среднего')
    else:
        print(f'Прибыль предприятия {key} - ниже среднего')
