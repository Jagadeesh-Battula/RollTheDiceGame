import random
s=input("Enter yes or y if you want to roll the dice again")
min_value=1
max_value=6
while(s=="yes" or s=="y"):
    n=random.randint(min_value,max_value)
    print(n)