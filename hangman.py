from replit import clear
import random
import hangman_art
import hangman_words
#Another way to do this:
#from hangman_words import word_list
#from hangman_art import logo, stages

word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
#Keep track of wrong guesses
wrong_guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
# Check that they've only entered one letter
    if len(guess) > 1:
      print("You can only guess one letter at a time.")

    elif guess in display or guess in wrong_guesses:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        wrong_guesses += guess
        print(f"{guess} isn't in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")
    print(f"Wrong guesses:  {' '.join(wrong_guesses)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])