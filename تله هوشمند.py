import math


def decimal2Base(num, b):
    r = ""
    while num > 0:
        remainder = int(num % b)
        num = num // b
        r = (str(remainder)) + r

    return r


k = input()
ts = 0
while k != "-1 -1":
    m = k.split()
    a = int(m[0])
    b = int(m[1])
    s = 0
    if b > 9 or b < 2:
        print("invalid base!")
        quit()
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            s += i
            if i != a // i:
                s += a // i
    ts = ts + int(decimal2Base(s, b))
    k = input()
print(ts)
