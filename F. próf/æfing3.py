#write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Input a positive integer: "))

new_list = []

for i in range(0,len(a)):
    if a[i] < num:
        new_list.append(a[i]) 
        print(a[i],"is less than 5. \n ")
    else:
        print(a[i],"is bigger than 5. \n ")

print(new_list)