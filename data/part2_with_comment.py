from collections import Counter
import numpy as np

data = {'A': [], 'B': [], 'C': []}
with open('../4731_my.csv') as f:
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


def check(l1, l2):
    return not Counter(l1) - Counter(l2)

#тест
"""
def finder():
    global ca,cb,cc
    count_data = {'A': 0, 'B': 0, 'C': 0}
    keys = list(data.keys())
    for key in keys:
        mass = data.get(key)
        for line in mass:
            if check(ans, line):
                count_data[key] += 1
    b = list(count_data.values())
    if sum(b) == 0:
        print("Это не А, не B и не C")
        quit()
    print(b)
    # print(max(count_data, key=count_data.get))
    if b[0]>b[1]and b[0]>b[2]:
        print("A")
        ca += 1
    elif b[1]>b[0]and b[1]>b[2]:
        print("B")
        cb += 1
    elif b[2]>b[0]and b[2]>b[1]:
        print("C")
        cc += 1
    elif b[0] != b[1] == b[2]:
        print("Это не А")
        cb += 1
        cc += 1
    elif b[1] != b[0] == b[2]:
        print("Это не B")
        ca += 1
        cc += 1
    elif b[2] != b[0] == b[1]:
        ca += 1
        cb += 1
        print("Это не C")
    else:
        ca += 1
        cb += 1
        cc +=1
        print('Это все')
    if ca > cb and ca>cc:
        print("A")
    elif cb > ca and cb > cc:
        print("B")
    elif cc > cb and cc > ca:
        print('C',ca, cb, cc)
    else:
        print("СОВПАЛИ") 
"""


def finder():
    count_data = {'A': 0, 'B': 0, 'C': 0}
    keys = list(data.keys())
    for key in keys:
        mass = data.get(key)
        for line in mass:
            if check(ans, line):
                count_data[key] += 1
    b = list(count_data.values())
    if sum(b) == 0:
        print("Это не А, не B и не C")
        quit()
    print(*count_data.items())
    # print(max(count_data, key=count_data.get))
    if b[0] > b[1] and b[0] > b[2]:
        print("Это A")
    elif b[1] > b[0] and b[1] > b[2]:
        print("Это B")
    elif b[2] > b[0] and b[2] > b[1]:
        print("Это C")
    elif b[0] != b[1] == b[2]:
        print("Это не А")
    elif b[1] != b[0] == b[2]:
        print("Это не B")
    elif b[2] != b[0] == b[1]:
        print("Это не C")
    else:
        print("Это все классы")


ans = []
for i in range(7):
    ans.append(int(input('Введите значение:')))
    finder()
