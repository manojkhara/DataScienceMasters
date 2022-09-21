#3. Write a Python Program to Print the Fibonacci sequence?
# 1,1,2,3,5,8
n = int(input("enter number: "))

def fibonacciHelper(n):
    if n <= 2:
        return 1
    return fibonacciHelper(n-1) + fibonacciHelper(n-2)

#print(fibonacciHelper(n))

def fibonacci(n):
    if n==1:
        return
    fibonacci(n-1)
    print(fibonacciHelper(n), end = ", ")

fibonacci(n)