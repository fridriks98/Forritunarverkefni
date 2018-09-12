#Verkefni_5
number = input("Please enter a number: ")
number_int = int(number)

if number_int >= 0:
    while number_int >= 1:
        print(number_int)
        number_int -= 1

    print("BOOM!")

