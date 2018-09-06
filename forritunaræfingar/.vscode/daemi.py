word = input("Enter a word: ")

while word != ".":
    print(word + "yay")
    word = input("Enter a word: ")
    print(word % len(word))


