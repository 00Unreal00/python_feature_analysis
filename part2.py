from collections import Counter


def rotate():
    for key in training_data.keys():
        sp = training_data.get(key)
        b = [[0 for _ in range(len(sp))] for _ in range(len(sp[0]))]
        for i in range(len(sp)):
            for j in range(len(sp[i])):
                b[j][i] = sp[i][j]
        training_data[key] = b


training_data = {'A': [], 'B': [], 'C': []}
with open('4731_my.csv') as f:
    keys = list(training_data.keys())
    change_pos = 0
    count = 0
    for _ in range(1, 46):
        line = list(map(int, f.readline().split()))
        if line[0] > count:
            count = line[0]
            training_data.get(keys[change_pos]).append(line[1:])
        else:
            count = 0
            change_pos += 1
            training_data.get(keys[change_pos]).append(line[1:])
    rotate()


def check(l1, l2):
    return Counter(l1) - Counter(l2)


def finder():
    a = list(training_data.keys())
    for i in a:
        fl = True
        b = training_data.get(i)
        for j in b:
            if not check(sings, j):
                print(i)
                fl = False
                break
        if not fl:
            break
    if fl:
        print('Не подходит ни под один')
        quit()

sings = []
for i in range(1, 4):
    sings.append(int(input("Введите признак:")))
    finder()



