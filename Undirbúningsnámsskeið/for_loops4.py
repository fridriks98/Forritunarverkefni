#Verkefni_4
low = input("Please input a number: ")
high = input("Please input a higher number: ")

Sum = 0

low_int = int(low)
high_int = int(high)

for x in range(low_int, high_int+1):

    if x % 2 == 0:
        
        Sum += x  

        print(x)    

print("The sum of the numbers is: ", Sum)