number_str = input("Number: ")
number = int(number_str)

guess_str = input("Guess a number: ")
guess = int(guess_str)

while 0 <= guess <= 100:
    if guess > number:
        print("Guessed Too High.")
    elif guess < number:
        print("Guessed Too Low.")
    else:
        print("You guessed it. The number was:" ,number)
        break
    
    guess_str = input("Guess a number: ")
    guess = int(guess_str)

else:
    print("You quit too early, the number was:",number)