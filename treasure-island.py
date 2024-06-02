import os
from ti_art import logo, boat, house, shark, flames, game_over, treasure, mimic, badger


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def game():
    game_is_over = False
    # Treasure Island - choose your own adventure
    print(logo)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice1 = input('You\'re at a cross road. Do you want to go left or right? \n').lower()
    if choice1 == "left":
        clear()
        print('As you wander down the left path for a while, you wonder if there is anything to see. \n'
              'Eventually, you come to a lake. \nThere\'s an island in the middle of the lake, '
              'and you suspect that might be where the treasure is. ')
        choice2 = input('Do you "wait" for a boat? Or do you "swim" across? \n').lower()
        if choice2 == "wait":
            clear()
            print("After waiting for what seemed like an eternity, a mysterious boat arrives and you embark.")
            print(boat)
            print("Whose boat is this? Who's navigating?\n"
                  "There are no answers, the only sound is the water quietly lapping against the boat.\n"
                  "You - amazingly - arrive at the island unharmed, and quickly disembark from the strange boat.")
            input("Press enter to continue")
            clear()
            print(house)
            choice3 = input("On the island, you approach a house and see 3 doors. One is red, one is yellow, "
                            "and one is blue. \nWhich door do you choose? \n").lower()
            if choice3 == "red":
                clear()
                print(f"As the door closes behind you, a trap activates and the room is engulfed in flames.\n"
                      f"{flames}"
                      f"\nYou die in agony. \n{game_over}")
                return game_is_over
            elif choice3 == "yellow":
                clear()
                print(f"As the door closes behind you, you see a chest in the opposite corner. "
                      f"{treasure}"
                      f"\nWhen you open it, you find riches beyond your wildest dreams! You Win!")
                return game_is_over
            elif choice3 == "blue":
                clear()
                print(f"As the door closes behind you, you see a chest in the opposite corner. \n"
                      f"When you go to open it, you find too late that it's a mimic."
                      f"{mimic}"
                      f"\nYou become its latest meal. \n{game_over}")
                return game_is_over
            else:
                print("You chose a door that doesn't exist and fall forever through the abyss. Game Over.")
                return game_is_over
        elif choice2 == "swim":
            clear()
            print(f"Since you're a strong swimmer, you decide to try the water; \nafter all, the island doesn't "
                  f"look *that* far. \nUnfortunately, the darkness hid the sharks below the surface, and you get "
                  f"attacked and eaten.\n{shark}{game_over}")
            return game_is_over
        else:
            print(f"You've wandered away from the adventure, and the treasure is nowhere to be found. \n{game_over}")
            return game_is_over
    elif choice1 == "right":
        clear()
        print(f"You turn right and walk for a while until you step on soft ground.\n"
              f"Though you stumble, you regain your footing. Whew, that was close! \n"
              f"Your heart sinks as you hear rustling behind you - that can't be good, and you start running.\n"
              f"A badger emerges, you stepped in its den! You're unable to outrun it and soon get gruesomely "
              f"mauled to death.\n{badger}{game_over}")
        return game_is_over
    else:
        print(f"You've wandered away from the adventure, and the treasure is nowhere to be found. \n{game_over}")


game()

while input("Do you want to play again? y or n ") == "y":
    clear()
    game()
