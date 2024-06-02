import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = '''
  ____            _      ____                         ____       _                        
 |  _ \ ___   ___| | __ |  _ \ __ _ _ __   ___ _ __  / ___|  ___(_)___ ___  ___  _ __ ___ 
 | |_) / _ \ / __| |/ / | |_) / _` | '_ \ / _ \ '__| \___ \ / __| / __/ __|/ _ \| '__/ __|
 |  _ < (_) | (__|   <  |  __/ (_| | |_) |  __/ |     ___) | (__| \__ \__ \ (_) | |  \__ \\
 |_| \_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_|    |____/ \___|_|___/___/\___/|_|  |___/
                                   |_|                                                    
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def game():
    comp_choice = random.randint(0, 2)
    print(logo)
    user_choice = int(input("Choose: \n   0 - Rock\n   1 - Paper\n   2 - Scissors\n"))
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
    else:
        print("You typed an invalid number. You lose!")
    print("Computer chose:")
    if comp_choice == 0:
        print(rock)
    elif comp_choice == 1:
        print(paper)
    elif comp_choice == 2:
        print(scissors)
    if user_choice == 0 and comp_choice == 2:
        print("You win!")
    elif user_choice == 2 and comp_choice == 1:
        print("You win!")
    elif user_choice == 1 and comp_choice == 0:
        print("You win!")
    elif user_choice == comp_choice:
        print("It's a draw!")
    else:
        print("You lose!")


game()

while input("Do you want to play again? y or n ") == "y":
    clear()
    game()
