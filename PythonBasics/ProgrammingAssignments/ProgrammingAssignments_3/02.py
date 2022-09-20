#2. Write a Python Program to Check if a Number is Odd or Even?

while True:
    num = int(input("enter number: "))
    if num>0:
        if num % 2 == 0:
            print("even")
        else:
            print("odd")
        break
    else:
        print("enter a positive number")
        continue
