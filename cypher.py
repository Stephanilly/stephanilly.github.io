# functions with arguments and parameters
# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}?")
# # greet_with("Angela", "London")
# # Function with keyword arguments
# greet_with(location="London", name="Angela")

# #Paint Area Calculator - how many cans of paint you need to cover a wall
# import math
# def paint_calc(height, width, cover):
#   number_of_cans = math.ceil((height * width) / cover)
#   print(f"You'll need {number_of_cans} cans of paint.")
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# #Prime number checker
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")
# n = int(input("Check this number: "))
# prime_checker(number=n)

#Caesar Cipher
from caesar_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  new_word = ""
  while shift > 25:
    shift -= 26
  for char in text:
      if char in alphabet:
          index = alphabet.index(char)
          if direction == "encode":
              new_index = index + shift
              if new_index > 25:
                  new_index -= 26
          elif direction == "decode":
              new_index = index - shift
              if new_index < 0:
                  new_index += 26
          new_letter = alphabet[new_index]
          new_word += new_letter
      else:
          new_word += char
  print(f"The {direction}d text is {new_word}")

cont = True
while cont:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  again = input("Do you want to go again?\n").lower()
  if not (again == "yes" or again == "y"):
    cont = False
    print("Goodbye")