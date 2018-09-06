n = int(input("Input an int: ")) # Do not change this line

factor = 1
# Fill in the missing code below
while factor <= n:
    if n % factor == 0:
        print(factor)
        factor += 1
    else:
        factor += 1
 