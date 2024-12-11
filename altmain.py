#Tried my hand (pun intended) at this again. Still couldn't manage a more elegant, less repetitive solution, but at least I made it work in the time I afforded myself.

import random

deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
PLAYER_HAND = []
DEALER_HAND = []
PLAYER_SCORE = 0
DEALER_SCORE = 0


def deal_new_card(hand):
    hand.append(random.choice(deck_of_cards))
    return hand


def adjust_score(hand):
    return sum(hand)


def ace_in_hand_and_over_21(hand, score):
    if score > 21 and 11 in hand:
        ace_index = hand.index(11)
        hand[ace_index] = 1
        score -= 10
    return hand, score


def check_for_blackjack(user_score, comp_score):
    if user_score == 21:
        if comp_score == 21:
            return "You have blackjack, but so does the Dealer. It's a tie!"
        else:
            return "You have blackjack! You win!"
    else:
        return False


def check_for_over_21(score):
    if score > 21:
        return "You went over 21. You are busted!"
    else:
        return False


def compare_scores(user_score, comp_score):
    if user_score == comp_score:
        return "It's a tie!"
    elif user_score > comp_score:
        return "You win!"
    else:
        return "The dealer wins."


big_loop = True
while big_loop:

    # Deal initial cards
    for _ in range(2):
        PLAYER_HAND = deal_new_card(PLAYER_HAND)
        DEALER_HAND = deal_new_card(DEALER_HAND)
    PLAYER_SCORE = adjust_score(PLAYER_HAND)

    # Check for ace
    check_for_ace = ace_in_hand_and_over_21(PLAYER_HAND, PLAYER_SCORE)
    PLAYER_HAND = check_for_ace[0]
    PLAYER_SCORE = check_for_ace[1]

    # Show cards
    print(f"Your hand is {PLAYER_HAND}. Your score is {PLAYER_SCORE}.")
    print(f"The dealer's first card is {DEALER_HAND[0]}.")

    # Check for blackjack
    blackjack = check_for_blackjack(PLAYER_SCORE, DEALER_SCORE)
    if blackjack:
        print(blackjack)
        big_loop = False
        break

    # Dealer check for ace
    comp_check_for_ace = ace_in_hand_and_over_21(DEALER_HAND, DEALER_SCORE)
    DEALER_HAND = comp_check_for_ace[0]
    DEALER_SCORE = comp_check_for_ace[1]

    # game loop
    game = True
    while game:
        choice = input("Would you like another card? Press 'h' for hit or any other key for stand: ").lower()
        if choice == "h":
            PLAYER_HAND = deal_new_card(PLAYER_HAND)
            PLAYER_SCORE = adjust_score(PLAYER_HAND)
            check_for_ace = ace_in_hand_and_over_21(PLAYER_HAND, PLAYER_SCORE)
            PLAYER_HAND = check_for_ace[0]
            PLAYER_SCORE = check_for_ace[1]
            print(f"Your hand is {PLAYER_HAND}. Your score is {PLAYER_SCORE}.")
            blackjack = check_for_blackjack(PLAYER_SCORE, DEALER_SCORE)
            if blackjack:
                print(blackjack)
                big_loop = False
                break
            busted = check_for_over_21(PLAYER_SCORE)
            if busted:
                print(busted)
                big_loop = False
                break
        else:
            if DEALER_SCORE == 21:
                print("The dealer has blackjack! Dealer wins!")
                game = False
            else:
                while DEALER_SCORE < 17:
                    DEALER_HAND = deal_new_card(DEALER_HAND)
                    DEALER_SCORE = adjust_score(DEALER_HAND)
                print(f"The dealer's cards are {DEALER_HAND}. The dealer has {DEALER_SCORE}.")
                if DEALER_SCORE > 21:
                    print("The dealer is busted. You win!")
                    big_loop = False
                    break
                else:
                    print(compare_scores(PLAYER_SCORE, DEALER_SCORE))
                    big_loop = False
                    break





