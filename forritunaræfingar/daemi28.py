#Create a program that takes an integer as input, let ́s call it turns. 
#This integer should indicate how many times the user wants to input a new integer. 
#Next the program should let the user input turnsmany integers. 
#The program should then print how many negative integers the user input and how many positive integers the user input.
number_of_intz = int(input("How many times do you want to input a new int? ")) 

new_num = 0
negative_int = 0
positive_int = 0
zeros = 0

for x in range(0,number_of_intz):
    new_num = int(input("Input an integer: "))
    if new_num < 0:
        negative_int += 1
    elif new_num > 0:
        positive_int += 1
    else:
        zeros += 1
print("The number of negative numbers is: ",negative_int)
print("The sum of positive numbers is: ",positive_int)  