#4. Write a Python Program to Check Prime Number?
num = int(input("enter a number"))
factors = 0
for i in range (2,num):
    if num % i == 0:
        factors += 1

if factors == 0:
    print("prime number")
else:
    print("composite number")
