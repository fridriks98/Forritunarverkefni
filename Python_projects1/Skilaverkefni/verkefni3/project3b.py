tala = int(input("Input a position between 1 and 10: "))
new_num = tala

while 0 < tala < 11: 
    print("""l - for moving left
r - for moving right
Any other letter for quitting""")
    breyting = input("Enter your choice: ")
    breyting = breyting.lower()
    if breyting == 'l' or breyting == 'r':
        if new_num == 1:
            if breyting == 'l':
                new_num = new_num
            elif breyting == 'r':
                new_num += 1    
        elif new_num == 10:
            if breyting == 'l':
                new_num -= 1
            elif breyting == 'r':
                new_num = new_num    
        else:    
            if breyting == 'l':
                new_num -= 1
            elif breyting == 'r':
                new_num += 1

        print("New position is:",new_num)
        
    else:
        print("New position is:",new_num)
        break


    

