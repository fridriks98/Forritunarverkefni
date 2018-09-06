name = input("Input a name: ")

name_change = name.split(', ')
last_word = name_change[0].capitalize()
lastname = last_word[0:len(last_word)]

first_name = name_change[1]

first_initial = first_name[:1].capitalize()

new_name = first_initial + ". " + lastname
print(new_name)
