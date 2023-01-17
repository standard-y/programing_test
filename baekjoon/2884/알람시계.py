a, b = map(int, input().split())

settime = 45
settime = int(settime)
h = 60
h = int(h)

if b >= settime:
    print(a, b - settime)
elif b < settime:
    print(a - 1 if a > 0 else a + 23, end =' ')
    print(h - (settime - b))
