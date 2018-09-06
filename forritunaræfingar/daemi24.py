#Create a program that takes 2 integers as input, let’s call them low and high. \
#Your program should print the sum of all the integers between low and high(low and high included)that are divisible by 3. \
#You may assume that lowis always lower than high.

low = int(input("Input the lower value: "))
high = int(input("Input the lower value: "))

the_sum = 0

for x in range(low, high+1):
    if x % 3 == 0:
        the_sum += x
print(the_sum)