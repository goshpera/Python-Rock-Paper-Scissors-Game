import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input, please try again.")

computer_num = random.randint(1, 3)
computer_move = ""

if computer_num == 1:
    computer_move = rock
elif computer_num == 2:
    computer_move = paper
elif computer_num == 3:
    computer_move = scissors

