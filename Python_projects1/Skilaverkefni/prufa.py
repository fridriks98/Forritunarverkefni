word = str(input("Enter a word: "))
first_letter = word[0] 

vowel = ["a","e","i","o","u", "A", "E", "I", "O", "U"]

word_length = len(word)

while word != ".":
    if first_letter in vowel:
        print(word+"yay")
    else:
        for x in range(word_length):
            first_letter = word[0] 
            word = word[1:] + first_letter
            if word[0] in vowel:
                print(word + "ay")
                break   
                             
    word = str(input("Enter a word: "))  


