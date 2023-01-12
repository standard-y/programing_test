lis = []
x = []
y = []

for i in range(19):
    lis.append([])
    for j in range(19):
        lis[i].append(0)
for i in range(19):
    go = list(map(int, input().split()))
    for j in range(19):
        lis[j][i] = go[j]

use = int(input())
for i in range(0, use):
    x, y = input().split()
    x= int(x)
    y = int(y)
    for j in range(19):
        lis[y-1][j] = int(not bool(lis[y-1][j]))
        for k in range(19):
            lis[k][x-1] = int(not bool(lis[k][x-1]))


for i in range(19):
    for j in range(19):
        print(lis[j][i], end=' ')
    print('')