ent = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    load = input().split()
    ent[i] = load

r, u = 1, 1
while (1):
    if ent[r][u] == '2':
        ent[r][u] = '9'
        break
    elif ent[r][u + 1] != '1':
        ent[r][u] = '9'
        u += 1
    elif ent[r + 1][u] != '1':
        ent[r][u] = '9'
        r += 1
    elif ent[r + 1][u + 1] == '1':
        ent[r][u] = '9'
        break
    

for i in range(10):
    for j in range(10):
        result = ent[i][j]
        print(int(result), end = ' ')
    print()