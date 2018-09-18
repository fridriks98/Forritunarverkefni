def count_case(a):
    upper = 0
    lower = 0
    for x in range(0, len(a)):
        if a[x].isupper():
            upper += 1
        
        elif a[x].islower():
            lower += 1

    return upper, lower
         

        
user_input = input("Enter a string: ")

a, b = count_case(user_input)

print("Upper case count: ", a)
print("Lower case count: ", b)