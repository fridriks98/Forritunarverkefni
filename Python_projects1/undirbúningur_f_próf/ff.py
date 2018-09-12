bla = "My name is Michelle"

bla_list = bla.split()
new_bla = ""
print(bla_list)
for x in range(3, -1,-1):
    word = bla_list[x]
    new_bla += word  +  " "

print(bla)
print(new_bla)