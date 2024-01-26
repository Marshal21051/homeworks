import numpy as np

n, m = input().split()
m = int(m)
n = int(n)
my_dict = {}

for x in range(n):
    my_arr = []
    for i in range(m):
        a = input().split()
        for j in range(m):
            a[j] = int(a[j])
        my_arr.append(a)
    my_dict[x] = my_arr


max, min = float('-inf'), float('inf')
mx_id = ""

for i in range(n):
    for j in range(n):
        if i != j:
            arr = np.matmul(my_dict[i], my_dict[j])
            dt = np.linalg.det(arr)
            if dt > max:
                max = dt
                mx_id = f'{i + 1} {j + 1}'

first, second = mx_id.split()[0], mx_id.split()[1]

dt1 = np.linalg.det(my_dict[int(first) - 1])
dt2 = np.linalg.det(my_dict[int(second) - 1])

if dt1 > dt2:
    res = np.matmul(my_dict[int(first) - 1], my_dict[int(second) - 1])
else:
    res = np.matmul(my_dict[int(first) - 1], my_dict[int(second) - 1])

# print(np.linalg.inv(res))

res = np.linalg.inv(res)

for i in range(m):
    for j in res[i]:
        print(f"{round(j, 3):.3f}", end=' ')
    print()
