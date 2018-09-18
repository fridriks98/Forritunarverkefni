def max(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return print(num1)
    elif num2 >= num3:
        return print(num2)
    else:
        return print(num3)    

max_num = 0

num1 = int(input("Input a positive integer: "))
num2 = int(input("Input a positive integer: "))
num3 = int(input("Input a positive integer: "))

max_num = max(num1,num2,num3)