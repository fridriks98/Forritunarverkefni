#Föll

def texti():
    print("l - for moving left"
    print("r - for moving right")
    print("Any other letter for quitting")

def breytt():
    return input("Enter your choice: ").lower()

def faersla(breyting, new_num):
    if breyting == 'l':
        new_num = new_num
    elif breyting == 'r':
        new_num += 1
    return new_num

def faersla1(breyting,new_num):
    if breyting == 'l':
        new_num -= 1
    elif breyting == 'r':
        new_num = new_num
    return new_num

def faersla2(breyting,new_num):
    if breyting == 'l':
        new_num -= 1
    elif breyting == 'r':
        new_num += 1
    return new_num




