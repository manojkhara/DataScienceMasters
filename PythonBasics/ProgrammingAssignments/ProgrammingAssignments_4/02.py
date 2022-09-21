#2. Write a Python Program to Display the multiplication Table?

num = int(input("enter number: "))
for i in range(1,11):
    print("{} * {} = {}".format(num,i,num*i) )