#1. Write a Python Program to Find the Factorial of a Number?

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

n = int(input("enter integer: "))
result  = factorial(n)
print(result)
