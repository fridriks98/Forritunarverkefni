#Create a program that lets the user input a single integer, lets call it multiplier. \
#Next your program should print all the integers between 2 and 15 (2 and 15 included) \
#multiplied by the value of multiplier.

multiplier = int(input("input an integer: "))

x = 2

while x <= 15:
    print(x * multiplier)
    x += 1
