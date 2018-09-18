def minimum_of_two(first, second):
    if first <= second:
        return first
    else:
        return second         

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

minimum = minimum_of_two(first,second)
    
print("Minimum: ", minimum)