m = int(input())
n = int(input())
k = int(input())

while n != 0:
    c = m & n
    m = m ^ n
    n = c << 1

print(m)
if m != k:
    print("NO")
else:
    print("YES")
