#Verkefni5
size = int(input("Please input the size of the list: "))

numbers_list = []

highest_value = 0

for x in range(size):
    
    number = int(input("Please enter a number: "))
    
    numbers_list.append(number)
    
    if highest_value < number:
        highest_value = number
        
print("This is the list: ",numbers_list)
print(highest_value)

