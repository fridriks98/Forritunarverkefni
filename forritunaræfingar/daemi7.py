#Create a program that accepts 2 integers as input and outputs the greater integer. \
#If the integers are equal the program should print the text “the numbers are equal”.
num1 = int(input("Input an integer: ")) 
num2 = int(input("Input another integer: ")) 

if num1 > num2:
    print(num1,"is bigger")
elif num2 > num1:
    print(num2,"is bigger")
else:
    print("The numbers are equal")
    
