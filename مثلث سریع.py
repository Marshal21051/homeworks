n = int(input())
i = 0
l = [1]
while i < n:
    for k in l:
        print(k, end=' ')
    print()
    last = 0
    for k in range(0, len(l)):
        temp = l[k]
        l[k] = last + l[k]
        last = temp
    l.append(1)
    i = i + 1
