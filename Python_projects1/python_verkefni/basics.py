years_str = input("Years: ") # do not change this line
years_int = int(years_str)

years_in_seconds = 31536000*years_int
birth = years_in_seconds//7
death = years_in_seconds//13
new_immigrants = years_in_seconds//35

US_population = 307357870

new_population = US_population + birth - death + new_immigrants


print("New population after",years_int, "years is"\
,int(new_population)) # do not change this line