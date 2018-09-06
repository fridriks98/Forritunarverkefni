#Verkefni3
size = int(input("Please input the size of the list: "))

numbers_list = []

Sum = 0

#Nota while loop nuna

while size > 0:
    
    number = int(input("Please input a number: "))
    numbers_list.append(number)
    Sum += number
    size -= 1
    

print("This is the list: ",numbers_list)
print("And this is the sum of the list: ", Sum)