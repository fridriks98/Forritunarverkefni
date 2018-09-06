#Create a program that takes 2 integers as input, let’s call them low and high. \
#Your program should print the sum of all the integers between low and high(low and high included). \
#You may assume that low is always lower than high.
low = int(input("Input the lower value: "))
high = int(input("Input the lower value: "))

the_sum = 0

for x in range(low, high+1):
    print("x is now: ",x)
    the_sum += x
    print("The sum is now: ",the_sum)
    print()
print(the_sum)