#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

num = int(input("enter a number: "))

if num < 0 :
    print("negative")
elif num == 0 :
    print("zero")
else:
    print("positive")