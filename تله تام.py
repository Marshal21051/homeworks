import math


def sum(l):
    r = 0
    for k in l:
        r = r + k
    return r


def average(l):
    r = sum(l)
    return round(r / len(l), 2)


def min(l):
    if len(l) == 0:
        return 0
    r = l[0]
    for k in l:
        if k < r:
            r = k
    return r


def max(l):
    if len(l) == 0:
        return 0
    r = l[0]
    for k in l:
        if k > r:
            r = k
    return r


def gcd(l):
    if len(l) == 0:
        return 0
    r = l[0]
    for k in l:
        r = math.gcd(r, k)
    return r


def lcd(l):
    if len(l) == 0:
        return 0
    r = l[0]
    for k in l:
        r = r * k // math.gcd(r, k)
    return r


o = "invalid command"
command = input()
if command != "sum" and command != "average" and command != "lcd" and command != "gcd" and command != "min" and command != "max":
    print(o)
    quit()
k = input()
l = []
while k != "end":
    l.append(int(k))
    k = input()


if command == "sum":
    o = sum(l)
elif command == "average":
    o = average(l)
elif command == "lcd":
    o = lcd(l)
elif command == "gcd":
    o = gcd(l)
elif command == "min":
    o = min(l)
elif command == "max":
    o = max(l)

print(o)
