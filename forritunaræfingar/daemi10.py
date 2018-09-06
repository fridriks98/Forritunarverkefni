#Create a program that takes 1 integer as input. The program should print \
#”Less than 10” if the input value is less than 10. If the input value is \
#greater than or equal to 10 and less than 20 it should print “between 10 and 20”. \
# If the input value is greater than or equal to 20 the program should print \
#“the value is too high!” and if the input value is less than 0 the program should print “too low”.

number = int(input("Input an integer: "))

if 0 <= number < 10:
    print("Less than 10")
elif 10 <= number < 20:
    print("Between 10 and 20")
elif 20 <= number:
    print("The value is too high!")
else:
    print("too low")
