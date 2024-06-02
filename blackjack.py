############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
import blackjack_art
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
def deal_card():
    card = random.choice(blackjack_art.cards)
    card_value = card["value"]
    card_art = card["art"]
    return [card_value, card_art]


# Create a function called compare() and pass in the user_score and computer_score.  
def compare(user_score, computer_score):
    # If the computer and user both have the same score, then it's a draw.
    if user_score == computer_score:
        return "Draw. :|"
    # If the user_score is over 21, then the user loses.
    elif user_score > 21:
        return "Bust! You lose! :("
    # If the computer has a blackjack (0), then the user loses.
    elif computer_score == 0:
        return "Dealer wins with a blackjack! :("
    # If the user has a blackjack (0), then the user wins.
    elif user_score == 0:
        return "You win with a blackjack! :)"
    # If the computer_score is over 21, then the computer loses.
    elif computer_score > 21:
        return "Dealer busts! You win! :)"
    # If none of the above, then the player with the highest score wins.
    elif user_score > computer_score:
        return "You win! :)"
    else:
        return "Dealer wins! :("


# Create a function called calculate_score() that takes a List of cards as input and returns the score.
def calculate_score(cards):
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and
    # return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21,
    # remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Deal the user and computer 2 cards each using deal_card() and append().
def play_game():
    print(blackjack_art.logo)
    # user_cards = []
    user_card_values = []
    user_card_art = []
    # computer_cards = []
    computer_card_values = []
    computer_card_art = []
    for x in range(2):
        user_cards = deal_card()
        user_card_values.append(user_cards[0])
        user_card_art.append(user_cards[1])
        # print(user_card_values)
        # print(user_card_art)
        # computer_cards.append(deal_card())
        computer_cards = deal_card()
        computer_card_values.append(computer_cards[0])
        computer_card_art.append(computer_cards[1])
        # print(computer_card_values)
        # print(computer_card_art)

    # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    computer_score = calculate_score(computer_card_values)
    print(f"  Dealer's first card is: {computer_card_art[0]}")
    is_game_over = False
    bust = False
    while not is_game_over:
        user_score = calculate_score(user_card_values)
        print(f"  Your cards: {' '.join(user_card_art)}, current score: {user_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            if user_score > 21:
                bust = True

        # If the game has not ended, ask the user if they want to draw another card.
        # If yes, then use the deal_card() function to add another card to the user_cards List.
        # If no, then the player's portion of the game has ended.
        else:
            hit = input("Do you want to draw another card? y or n ")
            if hit == "y":
                # user_cards.append(deal_card())
                user_cards = deal_card()
                user_card_values.append(user_cards[0])
                user_card_art.append(user_cards[1])
            else:
                is_game_over = True

    # Once the user is done, it's time to let the computer play.
    # The computer should keep drawing cards as long as it has a score less than 17.
    while not bust and computer_score != 0 and computer_score < 17:
        # computer_cards.append(deal_card())
        computer_cards = deal_card()
        computer_card_values.append(computer_cards[0])
        computer_card_art.append(computer_cards[1])
        computer_score = calculate_score(computer_card_values)

    print(f"  Your final hand: {' '.join(user_card_art)}, final score: {user_score}")
    print(f"  Dealer's final hand: {' '.join(computer_card_art)}, final score: {computer_score}")
    print(compare(user_score, computer_score))


play_game()
while input("Do you want to play another game of Blackjack? y or n ") == "y":
    clear()
    play_game()
