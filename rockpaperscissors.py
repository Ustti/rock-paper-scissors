import random 



while True:

    choices = ['scissors', 'rock', 'paper']

    computer = random.choice(choices)
    player = None


    while player not in choices:
        player = input('rock, paper, scissors\n').lower()



    if computer == player:
        print('computer:',computer)
        print('player:', player)
        print('tie')

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")



    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")




    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
    












