word = str(input("Enter a word: "))
first_letter = word[0] 

vowel = ["a","e","i","o","u", "A", "E", "I", "O", "U"]

word_length = len(word)
while word != ".":
    no_vowel = True
    org_word = word
    if word[0] in vowel:
        print(word+"yay")
        no_vowel = False
    else:
        for x in range(word_length): 
            first_letter = word[0]
            word = word[1:] + first_letter
            if word[0] in vowel:
                print(word + "ay")
                no_vowel = False
                break
        if no_vowel:
            print(org_word + "ay")                            
    word = str(input("Enter a word: "))  


