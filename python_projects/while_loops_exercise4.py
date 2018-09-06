#Verkefni_4
low = input("Please input a number: ")
high = input("Please input a higher number: ")

Sum = 0

low_int = int(low)
high_int = int(high)

while low_int <= high_int:

    if low_int % 2 == 0:
        
        Sum += low_int    

        print(low_int)    
    
    low_int += 1

print("The sum of the numbers is: ", Sum)