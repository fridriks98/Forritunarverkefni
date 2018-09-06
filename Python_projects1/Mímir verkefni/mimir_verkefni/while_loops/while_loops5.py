n = int(input("Input a natural number: ")) # Do not change this line

factor = 2
prime = True

while n > factor:
    if n % factor == 0:
        prime = False
        break
    factor += 1    
if prime:
    print("Prime")
else:
    print("!Prime")