#Verkefni_3
low = input("Please input a number: ")
high = input("Please input a higher number: ")

Sum = 0

low_int = int(low)
high_int = int(high)

while low_int <= high_int:
    
    Sum += low_int

    print("the value of low is: ",low_int)

    low_int += 1

print("The sum of the numbers is: ",Sum)
    
