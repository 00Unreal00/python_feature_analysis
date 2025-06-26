import numpy as np

data = {'A': [], 'B': [], 'C': []}
with open('4731_my.csv') as f:
    keys = list(data.keys())
    change_pos = 0
    count = 0
    fl = True
    while fl:
        line = list(map(int, f.readline().split()))
        if len(line) == 0:
            fl = False
        elif line[0] > count:
            count = line[0]
            data.get(keys[change_pos]).append(line[1:])
        else:
            count = 0
            change_pos += 1
            data.get(keys[change_pos]).append(line[1:])
    for i in keys:
        data[i] = np.array(data.get(i))


def fischer_one_class(one_class):
    # axis=0 это столбцы axis=1 строки sum сумма
    mean = np.mean(one_class, axis=0)  # среднее значение по столбцам
    std = np.std(one_class, axis=0)  # среднеквадратическое отклонение по столбцам оказывается это СТАНДАРТНОЕ отклонение
    ix = mean ** 2 / std ** 2  # информативность
    indexix = np.argsort(ix)  # сортирует массив и выдаёт список индексов в каком порядке отсортировалось
    return [indexix[0] + 1, ix[indexix[0]], indexix[1] + 1, ix[indexix[1]]]


fish = fischer_one_class(data.get("A"))
print(f"Первый самый малый признак: {fish[0]}, второй малый признак: {fish[2]}")
print(3467890)