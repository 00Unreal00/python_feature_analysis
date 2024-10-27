import numpy as np
import matplotlib.pyplot as plot
from collections import Counter
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


#графики
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
xasb = (xaa - xbb).reshape(1, 2)  # матрица 1 строка 2 столбца
xaab = (xaa + xbb).reshape(2, 1)  # матрица 2 строки 1 столбец
n = np.dot(xasb, xaab).item()  # получение простого числа из массива
x2 = [s for s in range(-100, 200, 5)]
x1 = [((-(s * xasb[0, 1]) + 0.5 * n) / xasb[0, 0]) for s in x2]
plot.plot(x1, x2, c='purple')
'''created by 00Unreal00
'''
# вторая прямая
xab = np.sum(data.get("A") + data.get("B"), axis=0) / (len(data.get("A")) * 2)
xab = np.array([xab[u[0] - 1], xab[u[2] - 1]])
xc2 = np.mean(data.get("C"), axis=0)
xc2 = np.array([xc2[u[0] - 1], xc2[u[2] - 1]])
xabsc = (xab - xc2).reshape(1, 2)  # матрица 1 строка 2 столбца
xabac = (xab + xc2).reshape(2, 1)  # матрица 2 строки 1 столбец
n = np.dot(xabsc, xabac).item()  # получение простого числа из массива
x11 = [((-(s * xabsc[0, 1]) + 0.5 * n) / xabsc[0, 0]) for s in x2]
plot.plot(x11, x2, c='brown')
plot.show()


def distance(pnt1, pnt2):
    d = np.sqrt(np.sum((pnt1 - pnt2) ** 2))
    return d


points = np.vstack([np.column_stack([xa, ya]), np.column_stack([xb, yb]), np.column_stack([xc, yc])])


def knn(point, k=5):  # k nearest neighbors - к ближайших соседей
    cls = np.array(['A'] * len(data.get("A")) + ['B']*len(data.get("B")) + ['C']*len(data.get("C")))
    dist = [[distance(point, p), cl] for p, cl in zip(points, cls)]
    dist = sorted(dist, key=lambda x: x[0])[1:k+1]
    print(dist)
    dist = [i[1] for i in dist]
    print(Counter(dist).most_common()[0][0])
knn(np.array([15,30]))