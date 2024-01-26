a = int(input())
b = int(input())

c = a ^ b
i = 0
while c > 0:
    if c % 2 == 1:
        i = i + 1
    c = c // 2

print(i)
