age = int(input("Input age: ")) # Do not change this line

ticket = 30.0

if age >= 65:
    ticket = ticket/2
elif age <= 5:
    ticket = 0.0

print(ticket)
