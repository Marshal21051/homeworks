nums = [int(num) for num in input().split()]
numsmap = {}
i = 0

while i < len(nums):
    numsmap[nums[i]] = i
    i += 1

n = int(input())
o = []
i = 0
while i < len(nums):
    x = n - nums[i]
    if x < 0 or nums[i] <= n // 2:
        i += 1
        continue
    if x in numsmap:
        o.append(i + numsmap[x])
    i += 1

if not o:
    print("Not Found!")
else:
    o.sort()
    for i in o:
        print(i)
