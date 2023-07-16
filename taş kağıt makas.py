import random

user_choice = int(input("choose scissors 2, rock 0 or paper 1 .\n"))

computer_choice = random.randint(0,2)
print(f"computer choose {computer_choice}")
if user_choice == 0 and computer_choice == 2:
  print("you win")
elif computer_choice == 0 and user_choice == 2:
  print("you lose")
elif computer_choice == 0 and user_choice == 1:
  print("you win")
elif computer_choice == 2 and user_choice == 1:
  print("you lose")
elif computer_choice == 1 and user_choice == 2:
  print("you win")
elif computer_choice == 1 and user_choice == 0:
  print("you lose")   
elif computer_choice > user_choice:
  print("you lose!")
elif computer_choice == user_choice:
  print("its draw")  
else :
  print("you typed invalid number you lose") 
  