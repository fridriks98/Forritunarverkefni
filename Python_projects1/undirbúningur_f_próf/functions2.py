def sum_of_list(listi):
    Sum = 0
    for x in listi:
        Sum += x
    return print(Sum)         

listi = []
tala = 0

for x in range(1,10):
    tala = int(input("input a number:"))
    listi.append(tala)

print(listi)

sum_of_list(listi)

