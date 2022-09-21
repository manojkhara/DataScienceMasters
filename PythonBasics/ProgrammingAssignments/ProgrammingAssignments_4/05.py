# 5. Write a Python Program to Find Armstrong Number in an Interval?

lowerRange = int(input("enter lower range: "))
upperRange = int(input("enter upper range: "))

for num in range(lowerRange,upperRange+1):
    power = 1
    while power < 10:
        inp = num
        summ = 0
        digitPower = 0
        while inp>0 & summ<num:
            digit = inp % 10
            digitPower = pow(digit,power)
            summ += digitPower
            inp //= 10

        if summ==num:
            print(num)
            break

        power += 1