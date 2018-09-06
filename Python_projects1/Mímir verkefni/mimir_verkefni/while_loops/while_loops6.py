num = int(input("input:"))

while num**2 < 1000 and num > 9:
    if (num**2 % 100) == num:
        print(num)
        break
    else:
        break