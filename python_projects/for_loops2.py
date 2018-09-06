#Verkefni2
low = input("Please input a number: ")
high = input("Please input a higher number: ")

low_int = int(low)
high_int = int(high)

for x in range(low_int, high_int + 1):
    if x % 2 == 1:
        print(x)
    

