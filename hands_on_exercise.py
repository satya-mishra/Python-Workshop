"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("Type=",type(pi),"value=",pi)



# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i>50:
    print("Value of i is greater than 50 and value of i=",i)
elif i<50:
    print("Value of i is less than 50 and value of i=",i)
else:
    print("Value of i is equal to 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit=="orange":
    print("Current collor is orange")
elif picked_fruit=="strawberry":
    print("Current collor of strawberry is dark red")
elif picked_fruit=="banana":
    print("Current collor of banana is dark Green")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
x=int(input("Enter 1st number:" ))
y=int(input("Enter 2nd number:" ))
def multiplies(x, y):
    result = x*y
    return result
print(x, "*", y, "=", multiplies(x, y))

# TODO: Now call the function a few times to calculate the following answers
def m1(a, b):
    value = a*b
    return value
print("12 x 96 =", m1(12, 96))

print("48 x 17 =", m1(48, 17))

print("196523 x 87323 =", m1(196523, 87323))
