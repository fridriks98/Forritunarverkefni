#Verkefni_1
number = input("Please enter a number: ")
number_int = int(number)

#Þarf ekki að hafa if_else
if number_int >= 0:
    while number_int >= 0:
        print(number_int)
        number_int -= 1

    print("Loop is finished")

elif number_int < 0:
    print()

