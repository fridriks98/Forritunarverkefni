s = input("Input a string: ")
s_length = len(s)
digit_str = ''

for x in range(s_length):
    if s[x].isdigit():
        digit_str += s[x]

print(digit_str)    