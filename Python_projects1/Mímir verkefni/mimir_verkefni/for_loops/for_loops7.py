top_num = int(input("Input a number between 0 and 999: "))

for x in range(0, top_num):                                 #I input a number and check whether it's a Armstrong number or not  
    if x < 10:                                              #first i will check which number from 0 to 9 is an A num, which are all of them
        if x**1 == x:
            print(x)
    elif 9 < x < 100:                                       #Then i will check which number from 10 to 99 is an A num, which are none.
        if (x//10)**2 + (x%10)**2 == x:                     #I do x//10 do find the front number and x%10 to find the second number 
            print(x) 
            
    elif 99 < x < 1000:                                     #Finally, i check the numbers from 100 to 999.
        if (x//100)**3 + ((x//10)%10)**3 + (x%10)**3 == x:  #To find first number = x//100 
            print(x)                                        #To find second = x//10(then i get first two)%10(get the one in the middle)
                                                            #To find third = x%10 

                                                            #An Armstrong number is a number that is equal to 
                                                            #the sum of its digits when each digit is raised to the number of digits.

                                                            #For example:

                                                            #6 is an Armstrong number because 6**1 = 6
                                                            #153 is an Armstrong number because 1**3 + 5**3 + 3**3 = 153