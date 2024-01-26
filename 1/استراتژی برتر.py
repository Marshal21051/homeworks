def isPrim(a):
    if(a <= 1):
        return False
    for i in range (2,int(a**0.5)+1):
        if(a % i == 0):
            return False
    return True

input = (input())
a = int(input.split()[0])
b = int(input.split()[1])

if(a <= b):
    print("main order - amount: " , end = "")
else:
    print("reverse order - amount: ",end = "")
    temp = a
    a = b
    b = temp

counter = 0

for i in range (a , b+1):
    if(isPrim(i)):
        counter = counter + 1

print(counter)
