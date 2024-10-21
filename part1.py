import numpy as np

data = {'A': [], 'B': [], 'C': []}
with open('5722.csv') as f:
    keys = list(data.keys())
    change_pos = 0
    count = 0
    for _ in range(1, 46):
        line = list(map(int, f.readline().split()))

        if line[0] > count:
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
    print(std)
    ix = mean ** 2 / std ** 2  # информативность
    print(ix)
    indexix = np.argsort(ix)  # сортирует массив и выдаёт список индексов в каком порядке отсортировалось
    # вар1
    # return int(indexix[0]), float(ix[indexix[0]]), int(indexix[1]), float(ix[indexix[1]]) кортеж получается
    # вар2
    # min1 = ix[indexix[0]]
    # min2 = ix[indexix[1]]
    # i1 = indexix[0]
    # i2 = indexix[1]
    # return min1, min2, i1, i2
    # вар3
    return [indexix[0] + 1, ix[indexix[0]], indexix[1] + 1, ix[indexix[1]]]


u = fischer_one_class(data.get("C"))
print(f"Первый самый малый признак: {u[0]}, второй малый признак: {u[2]}")
