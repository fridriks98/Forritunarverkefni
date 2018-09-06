#Verkefni4
size = int(input("Please input the size of the list: "))

numbers_list = []

Sum = 0

Average = 0

#keyrum size-sinnum og tökum inn tölur til að setja inní listann.
#Bætum tölunum inn í listann með append.

for x in range(size):
       
    number = int(input("Please enter a number: "))
    numbers_list.append(number)
    Sum += number

Average = Sum/size    

print("This is the list: ",numbers_list)
print("This is the sum of the list: ", Sum)
print("And the average of the numbers is: ", Average)