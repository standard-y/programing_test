f = input()
s = input()

for i in range(3, 0, -1):
    a = 0
    b = 1
    for j in range(3, 0, -1):
        a += int(f[j-1])*int(s[i-1])*b
        b *= 10
    print(a) 
print(int(f) * int(s))