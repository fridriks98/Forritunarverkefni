#Make a two-player Rock-Paper-Scissors game. 
#(Hint: Ask for player plays (using input), compare them, 
#print out a message of congratulations to the winner, and ask if the players want to start a new game)

player1 = input("Rock, paper or scissor? ")
player2 = input("Rock, paper or scissor? ")

p1 = player1.lower()
p2 = player2.lower()
play_again = ""

while play_again != 'n' or play_again != 'N':
    if p1 == 'rock' and p2 == 'scissor' or p2 == 'rock' and p1 == 'scissor':
        print("Rock wins!")
    elif p1 == 'rock' and p2 == 'paper' or p2 == 'rock' and p1 == 'paper':
        print("Paper wins!")
    elif p1 == 'scissor' and p2 =='paper' or p2 == 'scissor' and p1 =='paper':
        print("Scissor wins!")
    elif p1 == p2:
        print("Tie!")
    else:
        print('Invalid input')
    play_again = input("Do you want to play again? ")
    if play_again == 'y' or play_again == 'Y':
        player1 = input("Rock, paper or scissor? ")
        player2 = input("Rock, paper or scissor? ")
    else: 
        break


