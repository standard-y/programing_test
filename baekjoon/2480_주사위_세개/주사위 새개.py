#1~6 세개같으면 10000+눈x1000

a,b,c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b and a != c:
    print(1000 + a * 100)
elif a == c and a != b:
    print(1000 + a * 100)
elif b == c and a != b:
    print(1000 + b * 100)
else:
    MAX_NUM = max(a,b,c)
    print(MAX_NUM*100)