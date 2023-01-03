
# [1][1] 
# 
# [1][0]
# [1][-1]

go = []

go = input().split('\n')

num = []
for i in range(16):
    for j in range(16):
        num[i][j] = go[j]
        go.pop()

for i in range(len(num)):
    for j in range(len(num)):
        print(num[i][j])