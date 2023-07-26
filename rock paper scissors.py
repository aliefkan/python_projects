import random
choices = ["rock", "paper", "scissors"]
game = False
play = input("Would you like to play? Y/N")
if play.lower() == "y":
    game = True
player_score = 0
computer_score = 0
while game:
    computer_choice = random.choice(choices)
    player_choice = input("Please enter your choice(R-S-P): ")
    if (player_choice.lower() == "r" and computer_choice == "rock") or (player_choice.lower() == "s" and computer_choice == "scissors") or (player_choice.lower() == "p" and computer_choice == "paper"):
        print("You both picked same! Go again!")
    elif (player_choice.lower() == "r" and computer_choice == "scissors") or (player_choice.lower() == "s" and computer_choice == "paper") or (player_choice.lower() == "p" and computer_choice == "rock"):
        print("You won! Congratuliations!")
        more = input("Would you like to continue? Y/N")
        player_score += 1
        if more.lower() == "n":
            print(f"you:{player_score}\ncomputer {computer_score}")
            game = False
    else:
        print("You lost!")
        more = input("Would you like to continue? Y/N")
        computer_score += 1
        if more.lower() == "n":
            print(f"you:{player_score}\ncomputer {computer_score}")
            game = False