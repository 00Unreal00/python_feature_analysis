import numpy as np
import matplotlib.pyplot as plot
data = {'A': [], 'B': [], 'C': []}
with open('1361_e_artem.csv') as f:
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


def fischer_tree_class(class1, class2, class3):
    mean1 = np.mean(class1, axis=0)
    std1 = np.std(class1, axis=0)
    mean2 = np.mean(class2, axis=0)
    std2 = np.std(class2, axis=0)
    mean3 = np.mean(class3, axis=0)
    std3 = np.std(class3, axis=0)
    ix = (mean1 - mean2 - mean3) ** 2 / (std1 ** 2 + std2 ** 2 + std3 ** 2)
    print(ix)
    indexix = np.argsort(ix)
    return [indexix[-1]+1, ix[indexix[-1]], indexix[-2]+1, ix[indexix[-2]]]


u = fischer_tree_class(data.get("A"), data.get("B"), data.get("C"))
print(*u)
x1 = list(data.get("A")[:, u[0]-1])
y1 = list(data.get("A")[:, u[2]-1])
plot.scatter(x1, y1, c='red')
x2 = list(data.get("B")[:, u[0]-1])
y2 = list(data.get("B")[:, u[2]-1])
plot.scatter(x2, y2, c='blue')
x2 = list(data.get("C")[:, u[0]-1])
y2 = list(data.get("C")[:, u[2]-1])
plot.scatter(x2, y2, c='yellow')
plot.xlabel(f"Признак {u[0]}")
plot.ylabel(f"Признак {u[2]}")

plot.show()