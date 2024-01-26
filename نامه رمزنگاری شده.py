args = input().split()
l = list(range(len(args)))
for i in args:
    l[int(i[1:])] = i[0]

for i in l:
    print(i, end='')
