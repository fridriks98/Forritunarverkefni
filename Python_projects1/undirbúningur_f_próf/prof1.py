month = input("Month: ")
day = int(input("Day: "))

month_capitalized = month.capitalize()
string = month_capitalized + " " + str(day)

if month_capitalized == 'January' and day == 1:
    print("New year's day")
elif month_capitalized == 'June' and day == 17:
    print("National holiday")
elif month_capitalized == 'December' and day == 25:
    print("Christmas day")
else:
    print("Not a holiday")

#Or

if string == 'January 1':
    print("New year's day")
elif string == 'June 17':
    print("National holiday")
elif string == 'December 25':
    print("Christmas day")
else:
    print("Not a holiday")

