import random

message = "Choose between 'rock', 'paper' or 'scissors' (press 'q' at any time to quit): "

rock_paper_or_scissors = ["rock", "paper", "scissors"]

def janken():
    """Describe all the possibilities and outcomes of the game."""
    while True:
        player_input = input(message)
        randomizer = random.choice(rock_paper_or_scissors)
        
        if player_input in rock_paper_or_scissors:
            print(player_input.title() + " <> " + randomizer.title())
            if player_input == randomizer:
                print("Draw! Retry.")
            elif player_input == rock_paper_or_scissors[0] and randomizer == rock_paper_or_scissors[1]:
                print("You lose :(")
            elif player_input == rock_paper_or_scissors[0] and randomizer == rock_paper_or_scissors[2]:
                print("You win!")
            elif player_input == rock_paper_or_scissors[1] and randomizer == rock_paper_or_scissors[0]:
                print("You win!")
            elif player_input == rock_paper_or_scissors[1] and randomizer == rock_paper_or_scissors[2]:
                print("You lose :(")
            elif player_input == rock_paper_or_scissors[2] and randomizer == rock_paper_or_scissors[0]:
                print("You lose :(")
            elif player_input == rock_paper_or_scissors[2] and randomizer == rock_paper_or_scissors[1]:
                print("You win!")
        elif player_input == 'q':
            break
        else:
            print("Please choose between 'rock', 'paper' or 'scissors'!")
janken()