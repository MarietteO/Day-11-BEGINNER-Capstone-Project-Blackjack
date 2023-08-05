import random
from art import logo

user_score = 0
computer_score = 0

# Card deck with values
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def deal_card(player_cards):
    """Deals a card to the player's hand."""
    card = random.choice(card_deck)
    player_cards.append(card)
    return player_cards


def change_score(player_cards):
    """Calculates the score based on the given player's cards, considering the value of aces."""
    score = 0
    for card in player_cards:
        score += card
    if score > 21 and 11 in player_cards:
        score -= 10
    return score


def detect_blackjack(score):
    """Detects if the given score represents a blackjack (21)."""
    if score == 21:
        return True


def detect_bust(score):
    """Detects if the given score represents a bust (over 21)."""
    if score > 21:
        return True


def determine_winner(user_total, computer_total):
    """Determines the winner of the game based on the players' scores."""
    if user_total > computer_total:
        print("You win!")
    elif computer_total > user_total:
        print("The computer wins!")
    else:
        print("It's a draw!")

print(logo)
game_on = True
while game_on:
    play_game = input("Do you want to play a game of Blackjack? Type \"y\" for yes or any other key for no: ").lower()
    if play_game == "y":
        for _ in range(2):
            deal_card(user_cards)
        deal_card(computer_cards)
        user_score = change_score(user_cards)
        computer_score = change_score(computer_cards)
        print(f"Your cards are: {user_cards}. Your score is {user_score}.")
        print(f"The computer first card is {computer_cards[0]}.")
        if detect_blackjack(computer_score):
            print("The computer has blackjack. You lose.")
        elif detect_blackjack(user_score):
            print("You have blackjack. You win!")
        else:
            continue_game = True
            while continue_game:
                another_card = input("Would you like to draw another card? Type \"y\" for yes or any other key for "
                                     "no: ").lower()
                if another_card == "y":
                    deal_card(user_cards)
                    user_score = change_score(user_cards)
                    print(f"Your cards are: {user_cards}. Your score is {user_score}.")
                    if detect_blackjack(user_score):
                        print("You have blackjack. You win.")
                        continue_game = False
                    elif detect_bust(user_score):
                        print("You went over. You lose.")
                        continue_game = False
                else:
                    while computer_score <= 16:
                        deal_card(computer_cards)
                        computer_score = change_score(computer_cards)
                    print(f"Your cards are: {user_cards}. Your score is {user_score}.")
                    print(f"The computer's cards are {computer_cards}. The computer's score is {computer_score}.")
                    if detect_blackjack(computer_score):
                        print("The computer has blackjack. You lose.")
                        continue_game = False
                    elif detect_bust(computer_score):
                        print("The computer went over. You win!")
                        continue_game = False
                    else:
                        determine_winner(user_score, computer_score)
                        continue_game = False
    else:
        game_on = False
