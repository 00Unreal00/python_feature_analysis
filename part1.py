
def rotate():
    for key in data.keys():
        sp = data.get(key)
        b = [[0 for _ in range(len(sp))] for _ in range(len(sp[0]))]
        for i in range(len(sp)):
            for j in range(len(sp[i])):
                b[j][i] = sp[i][j]
        data[key] = b


data = {'A': [], 'B': [], 'C': []}
with open('Nikita.csv') as f:
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
    rotate()


#метод фишера для 1 класса
def fischer(kit):
    max1 = max2 = 10**10
    i1 = i2 = 0
    ans = []
    for i in range(len(kit)):
        mAx = sum(kit[i])/len(kit[i])
        gAx = (sum((j-mAx)**2 for j in kit[i])/len(kit[i]))**0.5
        Ix = mAx**2/gAx**2
        ans.append(Ix)
        if it < max1:
            max1 = min(Is,max1)
            i1 = i
        if it <= max2:
            max2 = min(Is,max2)
            i2 = i
    return ans


for key in data.keys():
    print(f'{key}:{fischer(data.get(key))}')







