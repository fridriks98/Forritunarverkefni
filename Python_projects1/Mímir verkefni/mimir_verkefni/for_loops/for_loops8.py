stars = int(input("Max number of stars: ")) #I input the maximum numbers  
                                            #of stars that i want to get in one line

stars_str = "*"                             #I create a variable with the value "*"

for x in range(1, stars):                   #Then i make a for loop from 1 to (the max of stars)-1 
    print(x*stars_str)                      #Then i print in every round x*stars_str

for y in range(stars, 0, -1):               #Then i create another for loop to go down again(from max stars to 1)
    print(y*stars_str)                      #And i print the same as in the first loop.
