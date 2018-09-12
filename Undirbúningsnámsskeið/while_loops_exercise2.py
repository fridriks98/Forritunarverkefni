#Verkefni2
low = input("Please input a number: ")
high = input("Please input a higher number: ")

low_int = int(low)
high_int = int(high)

if low_int%2 == 1:
    while low_int <= high_int:
        print(low_int)
        low_int += 2

elif low_int%2 == 0:
    low_int += 1

    while low_int <= high_int:
        print(low_int)
        low_int += 2

print("Finished")

#Getur líka verið svona:

while low_int <= high_int:
    if low_int % 2 == 1:
        print(low_int)
    low_int += 1

    
