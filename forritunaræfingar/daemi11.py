#Create a program that takes 2 integers as input, let’s call them a and b. \
#Next the user should be able to input another integer which we shall call choice. \
#If choiceis 1 then the program should add a and b together and print the result. \
#If choice is 2 the program should subtract b from a and print the result. \
#If choice is 3 the program should multiply a and b together and print the result. \
#If choice is any other number the program should print the text: “invalid input.”

a = int(input("Input an integer: "))
b = int(input("Input another integer: "))

choice = int(input("Choose what to do with the numbers: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
else:
    print("Invalid input")
