s = input("Input a float: ")
s_float = float(s)

s_justified = "{:>12.2f}".format(s_float)

print(s_justified)