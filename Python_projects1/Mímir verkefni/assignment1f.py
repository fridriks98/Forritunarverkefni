d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

the_sum = 0

if 6 >= d1 >= 1 and 6 >= d2 >= 1:
    the_sum = d1+d2

    if the_sum == 7 or the_sum == 11:
        print("Winner")
    elif the_sum == 2 or the_sum == 3 or the_sum == 12:
        print("Loser")
    else:
        print(the_sum)
else:
    print("Invalid input")
