#Create the same program as in assignment 20 with one change. \
#Now the text “you picked <value>” wherevalue is the number that was input \
#should only be printed if that value is an odd number.
turns = int(input("How many times do you want to input a new integer: "))

for x in range(0,turns):
    value = int(input("Input a value: "))
    if value % 2 == 1:
        print("you picked :",value)
    
    print()