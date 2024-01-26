n = int(input())
s = set()
while n > 0:
    n -= 1
    e = input()
    if e.count('@') == 0:
        continue
    me = e[e.index('@') + 1:]
    s.add(me)

l = sorted(s)
for i in l:
    print(i)
