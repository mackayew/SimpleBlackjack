import random
import os


suits = ['hearts', 'diamonds', 'clubs', 'spades']
cards = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
values = {"ace": 11, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10}
user_hand = []
dealer_hand = []
user_total = 0
dealer_total = 0


class Card:
    def __init__(self, card, value, suit):
        self.card = card
        self.value = value
        self.suit = suit


def blackjack():

    global values, cards, suits, user_hand, dealer_hand, user_total, dealer_total
    user_hand = []
    dealer_hand = []
    user_total = 0
    dealer_total = 0
    deck = []

    for n in range(3):
        deck += [Card(card, values[card], suit) for card in cards for suit in suits]

    os.system('cls')
    print("User Hand:")
    user_card = random.choice(deck)
    user_hand.append(user_card)
    deck.remove(user_card)
    user_total += user_card.value
    print("{} of {} ({})".format(user_card.card, user_card.suit, user_card.value))

    dealer_card = random.choice(deck)
    dealer_hand.append(dealer_card)
    deck.remove(dealer_card)
    dealer_total += dealer_card.value

    user_card = random.choice(deck)
    if user_hand[0].value == 11 and user_card.value == 11:
        user_card.value = 1
        user_total += user_card.value
    else:
        user_total += user_card.value
    user_hand.append(user_card)
    deck.remove(user_card)
    print("{} of {} ({})".format(user_card.card, user_card.suit, user_card.value))
    print("User total: ", user_total)
    print()

    print("Dealer Hand:")
    print("{} of {} ({})".format(dealer_card.card, dealer_card.suit, dealer_card.value))
    dealer_card = random.choice(deck)
    if dealer_hand[0].value == 11 and dealer_card.value == 11:
        dealer_card.value = 1
        dealer_total += dealer_card.value
    else:
        dealer_total += dealer_card.value
    dealer_hand.append(dealer_card)
    deck.remove(dealer_card)
    print("?")
    print()

    if user_total == 21:
        print_hands()
        print("Blackjack!!")
        return 0
    else:
        while user_total < 21:
            choice = input("(H)it or (S)tand? ")
            if choice.upper() == 'H':
                user_card = random.choice(deck)
                user_hand.append(user_card)
                deck.remove(user_card)
                user_total += user_card.value
            elif choice.upper() == 'S':
                break
            else:
                print("Please enter a valid option.")

            if user_total > 21:                         # Changes ace to 1
                for card_value in user_hand:
                    if card_value.value == 11:
                        card_value.value = 1
                        user_total -= 10
                        break
                if user_total > 21:                 # Keep an eye on this, looks more efficient but may not work
                    print_hands()
                    print("You lose!")
                    return 0

            os.system('cls')
            print("User hand: ")
            for a in user_hand:
                print("{} of {} ({})".format(a.card, a.suit, a.value))
            print(user_total)
            print()
            print("Dealer hand: ")
            print("{} of {} ({})".format(dealer_hand[0].card, dealer_hand[0].suit, dealer_hand[0].value))
            print("?")
            print()

    print()
    print("Dealer Hand:")
    for c in dealer_hand:
        print("{} of {} ({})".format(c.card, c.suit, c.value))
    print("Dealer total: ", dealer_total)
    print()

    while dealer_total < 17:
        dealer_card = random.choice(deck)
        dealer_hand.append(dealer_card)
        deck.remove(dealer_card)
        dealer_total += dealer_card.value

        if dealer_total > 21:
            for card_value_d in dealer_hand:
                if card_value_d.value == 11:
                    card_value_d.value = 1
                    dealer_total -= 10

        if dealer_total > 21:
            print_hands()
            print("Dealer busts!")
            return 0

        if dealer_total == 21:
            print_hands()
            print("Dealer wins!")
            return 0

    os.system('cls')
    if user_total > dealer_total:
        print_hands()
        print("User wins!")
    elif dealer_total > user_total:
        print_hands()
        print("Dealer wins!")
    else:
        print_hands()
        print("Push!")


def print_hands():
    global user_hand, dealer_hand, user_total, dealer_total

    os.system('cls')
    print("User hand: ")
    for g in user_hand:
        print("{} of {} ({})".format(g.card, g.suit, g.value))
    print(user_total)
    print()
    print("Dealer hand: ")
    for h in dealer_hand:
        print("{} of {} ({})".format(h.card, h.suit, h.value))
    print(dealer_total)
    print()
