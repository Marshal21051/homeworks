a = int(input())
b = int(input())

a = a + (b << 32)
l = []

while a > 0:
    l.append(a % 2)
    a = a // 2

while len(l) < 64 :
    l.append(0)

b = int(input())
while b > 0:
    t = int(input())
    if l[t] == 0 :
        print("no")
    else:
        print("yes")
    b = b - 1
