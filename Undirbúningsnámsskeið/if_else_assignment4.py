#Verkefni_6
a = input("Please enter a number: ")
b = input("Please enter another number: ")
c = input("Please enter another number: ")

a_int = int(a)
b_int = int(b)
c_int = int(c)

if c_int == a_int*b_int:
    print("Good Job!")

elif c_int != a_int*b_int:
    print("Not quite right, go practice!")  