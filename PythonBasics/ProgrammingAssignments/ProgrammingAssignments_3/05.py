#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
#checking for odd numbers only because except 2 all the even numbers are composite
primeArr = []
for num in range(1, 10000 + 1, 2):     
    for i in range(2, num):
        if (num % i) == 0:
            break       # break the inner loop if it got divided
    else:
        primeArr.append(num)
print(len(primeArr))
print(primeArr)

