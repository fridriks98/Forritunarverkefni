top_num = int(input("Upper number for the range: ")) # Do not change this line

sum_of_divisors = 0

for number in range(1, top_num+1): # Im gonna find if there is any perfect number in the interval [1-top_num]
    for divisor in range(1, number): # to do that, im going to divide the number with every number that is smaller than that number
        if number % divisor == 0: # if the remainder is 0 im going to add that \
            sum_of_divisors += divisor #divisor, that gave me the remainder 0 to sum_of_divisors
    if number == sum_of_divisors: # When im finished dividing the number with all the divisors, im going to \
        print(number)   #check if the number and sum_of_divisors are the same number.
    
    sum_of_divisors = 0 #For every new number i check whether it's perfect, im going to change\
                        # sum_of_divisors back to zero.
                    

    