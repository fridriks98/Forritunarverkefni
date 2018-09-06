s = input("Input a string: ")
s_low = s.lower() 
target = 'o'

for index,letter in enumerate(s_low):
    if letter == target:
        print(index)

    