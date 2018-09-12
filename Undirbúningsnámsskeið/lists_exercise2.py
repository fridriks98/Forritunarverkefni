#Verkefni2

size = int(input("Please input the size of the list: "))

numbers_list = []

#keyrum size-sinnum og tökum inn tölur til að setja inní listann.
#Bætum tölunum inn í listann með append.

for x in range(size):
    number = int(input("Please enter a number: "))
    numbers_list.append(number)

print(numbers_list)
