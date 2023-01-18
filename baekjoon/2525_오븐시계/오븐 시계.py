h, m = map(int, input().split())
cook = int(input())
m += h * 60 + cook
print(m // 60 - 24 if m // 60 >= 24 else m // 60, m % 60)