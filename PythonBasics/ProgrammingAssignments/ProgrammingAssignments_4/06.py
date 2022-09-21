#6. Write a Python Program to Find the Sum of Natural Numbers?

def sumOfN(n):
    if n==1:
        return 1
    return n + sumOfN(n-1)

num = int(input("enter integer: "))
result = sumOfN(num)
print(result)