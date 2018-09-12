#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when divided by 2?

number = int(input("Enter a positive integer: "))

if number % 2 == 1:
    print("The number",number,"is odd.")
else:
    if number % 4 == 0:
        print("The number",number,"is even.")

    else:
        print("The number",number,"is even and is a multiple of 4.")
