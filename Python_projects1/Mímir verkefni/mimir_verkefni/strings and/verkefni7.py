my_int = input('Give me an int >= 0: ')
quotient = 0
remainder = 0
int_change = int(my_int)
bstr = ""

if my_int == '0':
    bstr += my_int
    print("The binary of", my_int, "is", bstr)    

else:    
    while int_change > 0:
        print("my int is now: ",int_change)
        quotient = int_change//2
        print("my int divided by 2: ",quotient)
        remainder = int_change % 2
        print("And the remainder is: ",remainder)
        bstr += str(remainder)
        int_change = quotient

    print("The binary of", my_int, "is", bstr[::-1])
