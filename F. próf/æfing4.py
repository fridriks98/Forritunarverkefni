#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Input an integer: "))
sum_of_divisors = 0

for divisor in range(1,num+1):
    if num % divisor == 0:
        print("The divisor",divisor,"divides evenly into the number",num )
        print()
        sum_of_divisors += 1

    divisor += 1

print(num,"has",sum_of_divisors,"divisors!")
