#Create a program that takes an integer as input, let's call it turns. \
#This integer should indicate how many times the user wants to input a new integer. \
#Next the program should let the user input turns many integers. \
#For each input value the program should print “you picked <value>” where value is the integer the user input. \
#So if the user inputs 3 to begin with that means that the variable \
#turnsshould get the value 3 and the user should be able to input 3 more integers.
turns = int(input("How many times do you want to input a new integer: "))

for x in range(0,turns):
    value = int(input("Input a value: "))
    print("you picked :",value)
