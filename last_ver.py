import numpy as np
import sys
from collections import defaultdict

np.set_printoptions(threshold=sys.maxsize)
data = {'A': [], 'B': [], 'C': [], 'D': []}
with open('451289A.csv') as f:
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
            data.get(keys[change_pos]).append(np.array(line[1:]))


def print_matrix(m):
    matrix = []
    print("Признаки:  |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |  10  |")
    for i in m:
        matrix.append(list(map(float, i)))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = str(m[i][j]) + (5 - len(str(m[i][j]))) * " " + "|"
            if i == j:
                m[i][i] = -10
        if i < 9:
            print(f"Признак {i + 1}  |", *matrix[i])
        else:
            print(f"Признак {i + 1} |", *matrix[i])

    return m


matr = np.round(np.corrcoef(np.array(data.get("A")), rowvar=False), 2)
matr[(matr == 1) & ~np.eye(matr.shape[0], dtype=bool)] = 0.99
matr = print_matrix(matr)
pairs = []
max_index = list(np.unravel_index(np.argmax(matr), matr.shape))
pairs.append([max_index.copy(), matr.max()])
while len(pairs) != len(matr)-1:
    matr[max_index[0]][max_index[1]] = -10
    matr[max_index[1]][max_index[0]] = -10
    l1 = matr[max_index[0]]
    l2 = matr[max_index[1]]
    if max(l1) > max(l2):
        matr[max_index[1], :] = -10
        matr[:, max_index[1]] = -10
        l1[max_index[1]] = -10
        max_index[1] = l1.argmax()
        pairs.append([max_index.copy(), l1.max()])
    else:
        matr[max_index[0], :] = -10
        matr[:, max_index[0]] = -10
        l2[max_index[0]] = -10
        max_index[0] = l2.argmax()
        pairs.append([max_index.copy(), l2.max()])
while True:
    try:
        r = float(input("Введите граничное значение\n"))
        break
    except:
        print("Неверно введено значение")
for i in pairs:
    print(i)
gr = defaultdict(list)
for (x, y), crit in pairs:
    if crit >= r:
        gr[x].append(y)
        gr[y].append(x)
visited = set()
groups = []


def dfs(start, group):
    visited.add(start)
    group.append(start)
    for n in gr[start]:
        if n not in visited:
            dfs(n, group)
    return group


for n in gr:
    if n not in visited:
        groups.append(sorted(dfs(n, [])))
for i in range(len(matr)):
    fl = False
    for sp in groups:
        if i in sp:
            fl = True
            break
    if not fl:
        groups.append([i])

for i, group in enumerate(groups):
    print(f"Группа {i + 1}:", *[i + 1 for i in group])
