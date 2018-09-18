def product_of_list(listi):
    product = 1
    for x in listi:
        product *= x
    return print(product)         

listi = []
tala = 0

counter = int(input("Input how many numbers you want in the list: "))

for x in range(0,counter):
    tala = int(input("input a number: "))
    listi.append(tala)

print('\n')
print(listi)

print("The product of the list is: ",end=' ')
product_of_list(listi)
