import numpy as np
import matplotlib.pyplot as plot

data = {'A': [], 'B': [], 'C': []}
with open('data/1361_e_artem.csv') as f:
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


def fischer_tree_class(class1, class2, class3):
    mean1 = np.mean(class1, axis=0)
    std1 = np.std(class1, axis=0)
    mean2 = np.mean(class2, axis=0)
    std2 = np.std(class2, axis=0)
    mean3 = np.mean(class3, axis=0)
    std3 = np.std(class3, axis=0)
    ix = (mean1 - mean2 - mean3) ** 2 / (std1 ** 2 + std2 ** 2 + std3 ** 2)
    indexix = np.argsort(ix)
    return [indexix[-1] + 1, ix[indexix[-1]], indexix[-2] + 1, ix[indexix[-2]]]


u = fischer_tree_class(data.get("A"), data.get("B"), data.get("C"))
print(f"Признак {u[0]} {u[1]} Признак {u[2]} {u[3]}")
xa = data.get("A")[:, u[0] - 1]
ya = data.get("A")[:, u[2] - 1]
plot.scatter(xa, ya, c='red')
xb = data.get("B")[:, u[0] - 1]
yb = data.get("B")[:, u[2] - 1]
plot.scatter(xb, yb, c='blue')
xc = data.get("C")[:, u[0] - 1]
yc = data.get("C")[:, u[2] - 1]
plot.scatter(xc, yc, c='green')
plot.xlabel(f"Признак {u[0]} {u[1]}")
plot.ylabel(f"Признак {u[2]} {u[3]}")

'''
F = (Xa-Xb) * X` - 1/2 * (Xa-Xb) * (Xa+Xb)`
F = xasb * X` - 1/2 * xasb * xaab`
xasb * X` - 1/2 * xasb * xaab` = 0
xasb[0,0] * x1 + xasb[0,1] * x2 - 1/2 * 20 = 0
x1 = (-(x2 * xasd[0,1]) + 1/2 * xaab)/xasd[0,0]

'''
# трэш какой-то я с утра забуду чо это за ужас
xaa = np.mean(data.get("A"), axis=0)
xaa = np.array([xaa[u[0] - 1], xaa[u[2] - 1]])
xbb = np.mean(data.get("B"), axis=0)
xbb = np.array([xbb[u[0] - 1], xbb[u[2] - 1]])
# xaa = np.array([1.5, 1.5])
# xbb = np.array([3.5, 3.5])
xasb = (xaa - xbb).reshape(1, 2)  # матрица 1 строка 2 столбца
xaab = (xaa + xbb).reshape(2, 1)  # матрица 2 строки 1 столбец
qq = np.dot(xasb, xaab).item()  # получение простого числа из массива
x2 = [s for s in range(-100, 100, 5)]
x1 = [((-(s * xasb[0, 1]) + 0.5 * qq) / xasb[0, 0]) for s in x2]
plot.plot(x1, x2)

# вторая прямая
xab = np.mean(data.get("A"), axis=0)+np.mean(data.get("B"), axis=0)
xab = np.array([xab[u[0] - 1], xab[u[2] - 1]])
xc = np.mean(data.get("C"), axis=0)
xc = np.array([xc[u[0] - 1], xc[u[2] - 1]])
xabsc = (xab - xc).reshape(1, 2)  # матрица 1 строка 2 столбца
xabac = (xab + xc).reshape(2, 1)  # матрица 2 строки 1 столбец
q = np.dot(xabsc, xabac).item()  # получение простого числа из массива
x22 = [s for s in range(-100, 100, 5)]
x11 = [((-(s * xasb[0, 1]) + 0.5 * q) / xasb[0, 0]) for s in x22]
plot.plot(x11, x22)
plot.show()

