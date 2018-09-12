#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
counter = int(input("How often do you want to print this exercise? "))

year = 2018

for x in range(0,counter):
    Name = input("What is your name? ")
    age = int(input("How old are you? "))
    turn_100 = 100 - age
    year_turn_100 = year + turn_100
    print(Name,"turns 100 in the year",year_turn_100)
    print()

