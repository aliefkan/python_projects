import random
game = False
play = input("Would you like to play a game?(Y/N)")
if play.lower() == "y":
    game = True
else:
    pass
tries = 0
while game:
    tries += 1
    the_random_number = random.randint(0, 100)
    player_guess = input("Guess a number 0 to 100: ")
    if player_guess.isdigit() is False:
        print("You should enter a number.")
    elif int(player_guess) == the_random_number:
        print(f"Congratulations! You did it in {tries} try!")
        game = False
    else:
        print("Wrong guess! Try again.")
