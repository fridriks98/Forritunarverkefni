num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

max_int = 0

if num1 > num2 and num1 > num3:  #Or I can put >= in front of everything
    max_int = num1               #But that is longer. This is shorther.   
elif num2 > num3:
    max_int = num2
else:
    max_int = num3

print("The maximum is: ", max_int) # Do not change this line
