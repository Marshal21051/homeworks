col = int(input())
l = ["*"]
for _ in range(col - 1): l.append(".")
colNow = 0
ch = input()

while ch != "END":
    if ch == "B":
        for k in l:
            print(k, end=" ")
        print()
        for i in range(len(l)): l[i] = "."
        l[colNow] = "*"

    elif ch == "R" and colNow + 1 < col:
        colNow += 1
        l[colNow] = "*"

    elif ch == "L" and colNow - 1 >= 0:
        colNow -= 1
        l[colNow] = "*"

    ch = input()

for k in l:
    print(k, end=" ")

if colNow + 1 != col: print("\nThere's no way out!")
