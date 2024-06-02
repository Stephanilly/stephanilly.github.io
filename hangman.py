import random
import hangman_art
import hangman_words
# Another way to do this:
# from hangman_words import word_list
# from hangman_art import logo, stages
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def game():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    print(logo)
    end_of_game = False
    lives = 6
    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"
    # Keep track of wrong guesses
    wrong_guesses = []
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # Check that they've only entered one letter
        if len(guess) > 1:
            print("You can only guess one letter at a time.")
        # Check that the letter hasn't been used already
        elif guess in display or guess in wrong_guesses:
            print(f"You've already guessed {guess}")
        # Check guessed letter
        else:
            clear()
            for position in range(word_length):
                letter = chosen_word[position]
                # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                if letter == guess:
                    display[position] = letter

            # Check if user is wrong.
            if guess not in chosen_word:
                wrong_guesses += guess
                lives -= 1
                print(f"{guess} isn't in the word. {lives} guesses left.\n")
                if lives == 0:
                    print(f"\nYou lose. The word was {chosen_word}\n")
                    end_of_game = True

            # Join all the elements in the list and turn it into a String.
            print(f"{' '.join(display)}\n")
            print(f"Wrong guesses:  {' '.join(wrong_guesses)}")
            print(stages[lives])

            # Check if user has got all letters.
            if "_" not in display:
                print("\nYou win!\n")
                end_of_game = True


word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo


# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

game()


# Give the player a choice to play again
while input("Do you want to play again? y or n: ") == "y":
    clear()
    game()
