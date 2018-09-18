def is_prime(a):
    for x in range(2,a):
        if a % x == 0:
            return False
    return True

    
num = int(input("Input an integer greater than 1: "))

if is_prime(num):
    print(num,"is a prime")
else:
    print(num,"is not a prime")