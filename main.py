from blackjack import *

# A simple text-based blackjack game
# Plans to add both a betting function and a GUI in the near future
# Ethan Mackay


while True:
    blackjack()

    print()
    ans = input("Play again? (y/n) ")
    while ans != 'y':
        if ans == 'n':
            quit()
        else:
            ans = input("Please enter a valid answer: ")
