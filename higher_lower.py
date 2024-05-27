import random
from hl_game_data import data
from hl_art import logo, vs
from replit import clear

choice1 = random.choice(data)
choice2 = random.choice(data)
if choice1 == choice2:
  choice2 = random.choice(data)
# print(choice1)
# print(choice2)

# Print the formatted choice comparison 
def print_choices(choice1, choice2):
  name1 = choice1["name"]
  count1 = choice1["follower_count"]
  desc1 = choice1["description"].lower()
  country1 = choice1["country"]

  name2 = choice2["name"]
  count2 = choice2["follower_count"]
  desc2 = choice2["description"].lower()
  country2 = choice2["country"]
  print(f"Compare A: {name1}, a {desc1}, from {country1}")
  print(vs)
  print(f"Against B: {name2}, a {desc2}, from {country2}")
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  return [guess, count1, count2]

# Evaluate the guess
def evaluate_guess(guess, count1, count2):
  """Takes the guess and the follower counts and returns True if the guess is correct"""
  if guess == "a" and count1 > count2:
    return True
  elif guess == "b" and count2 > count1:
    return True
  else:
    return False


def game(choice1, choice2):
  score = 0
  game_over = False
  while not game_over:
    print(logo)
    choices = print_choices(choice1, choice2)
    guess = choices[0]
    count1 = choices[1]
    count2 = choices[2]
    correct = evaluate_guess(guess, count1, count2)
    if correct:
      clear()
      score += 1
      print(f"\nYou're right! Current score: {score}")
      choice1 = choice2
      choice2 = random.choice(data)
      if choice1 == choice2:
        choice2 = random.choice(data)
    else:
      clear()
      print(logo)
      print(f"\nSorry, that's wrong. Final score: {score}")
      game_over = True
      again = input("Would you like to play again? y or n ").lower()
      if again == "y":
        clear()
        choice1 = random.choice(data)
        choice2 = random.choice(data)
        if choice1 == choice2:
          choice2 = random.choice(data)
        game(choice1, choice2)

game(choice1, choice2)