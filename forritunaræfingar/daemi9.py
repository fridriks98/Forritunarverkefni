#Create a program that takes 3 integers as input and prints the integer with the lowest value.
num1 = int(input("Input a positive integer: "))
num2 = int(input("Input another positive integer: "))
num3 = int(input("Input another positive integer: "))

if num1 <= num2 and num1 <= num3:
    print(num1)
elif num2 <= num1 and num2 <= num3:
    print(num2)
elif num3 <= num2 and num3 <= num1:
    print(num3)
    
