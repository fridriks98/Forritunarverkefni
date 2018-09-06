#Create a program that takes 2 integers as input, let’s call them low and high. \
#Your program should output all the integers between lowand high but \
#only if the value of low is lower than the value of high. (if printed the values of lowand highshould be included).
low = int(input("Input the lower interval: "))
high = int(input("Input the higher interval: "))

if high >= low:
    for x in range(low, high+1):
        print(x)
else:
    print("Invalid input")        
