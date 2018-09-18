def palindrome(a):
    new_str = ''
    for x in a:
        if x.isalpha():
            new_str += x
    
    return new_str



in_str = input("Enter a string: ")
str_low = in_str.lower()

new_str = palindrome(str_low)

if new_str == new_str[::-1]:
    in_str = '"' + in_str + '"'  
    print(in_str,"is a palindrome.")
else:
    in_str = '"' + in_str + '"'  
    print(in_str,"is not a palindrome.")



# call the function and print out the appropriate message