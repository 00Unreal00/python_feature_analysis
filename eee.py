file_open = open('data/5722.csv')
c_pr = []
with open('data/5722.csv') as f:
    for i in range(1, 46):
        if i < 31:
            f.readline()
        if i > 30:
            c_pr.append(list(map(int, f.readline().split()))[1:])

print(c_pr)

min_c_1, min_c_2 = 10**100, 10**100

ans = []
for stolbec in range(len(c_pr[0])):
    m_c, g_c, Ic = 0, 0, 0
    for obj in c_pr:
        m_c += obj[stolbec]
    m_c = m_c/len(c_pr)
    for obj in c_pr:
        g_c += (obj[stolbec]-m_c)**2
    g_c = (g_c/len(c_pr))**0.5

    Ic = m_c ** 2 / g_c ** 2
    # print("Ic: ", Ic, m_c, g_c)
    ans.append(Ic)
    if Ic < min_c_1:
        min_c_1 = Ic
        min_c_2 = min_c_1
        i1 = stolbec
    if Ic <= min_c_2:
        min_c_2 = min(Ic, min_c_2)
        i2 = stolbec
print(ans)
print(f"mins: {i1+1} {i2+1}")
print(f"C:{min_c_1} {min_c_2}")
