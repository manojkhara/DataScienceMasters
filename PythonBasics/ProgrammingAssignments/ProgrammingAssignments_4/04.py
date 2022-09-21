#4. Write a Python Program to Check Armstrong Number?
# sum of cubes of digits
# 153 = 1^3 + 5^3 + 3^3
#       1 + 125 + 27  =   153

#1634 = 1^4 + 6^4 + 3^4 + 4^4
#        1  + 1296 + 81 + 256 = 1634

#https://mathworld.wolfram.com/NarcissisticNumber.html
#https://mathlair.allfunandgames.ca/armstrong.php

num = int(input("enter number: "))
power = 1
while power < 10:
    inp = num
    summ = 0
    digitPower = 0
    while inp>0  :
        digit = inp % 10
        digitPower = pow(digit,power)
        summ += digitPower
        inp //= 10

    if summ==num:
        print(f"{num} is an armstrong number")
        print(f"power each digit by {power} and sum it")
        break

    power += 1

else:
    print(f"{num} is an not an armstrong number  ", power)