#Create a program that takes an integer as input, let ́s call it turns. 
#This integer should indicate how many times the user wants to input a new integer. 
#Next the program should let the user input turnsmany integers. 
#The program should then print the sum of all the negative integers the user input.
number_of_intz = int(input("How many times do you want to input a new int? ")) 

new_num = 0
negative_int = 0

for x in range(0,number_of_intz):
    new_num = int(input("Input an integer: "))
    if new_num < 0:
        negative_int += new_num

print("The sum of negative number is: ",negative_int)  