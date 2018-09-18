def number_range(a):
    if 1 < a < 555:
        return print(a,"is in range.")
    else:
        return print(a,"is outside the range!")
        
num = int(input("Enter a number: "))

number_range(num)