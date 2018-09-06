#Create a program that takes 2 integers as input, let’s call them low and high. \
#Your program should print all the integers between low and high (low and high included). \
#You may assume that low is always lower than high.
low = int(input("Input the lower interval: "))
high = int(input("Input the higher interval: "))

for x in range(low,high+1):
    print(x)

#or
print()

a = low

while a <= high:
    print(a)
    a += 1
