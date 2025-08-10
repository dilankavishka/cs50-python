#import random

#coin = random.choice(["heads", "tails"])
#print(f"The coin landed on: {coin}")

from random import choice
from random import randint
from random import shuffle

coin = choice (["heads", "tails"])
print(f"The coin landed on: {coin}")

number = randint (1, 20)
print(f"The random number is: {number}")

deck = [("Jack", "Hearts"), ("Queen", "Diamonds"), ("King", "Clubs"), ("Ace", "Spades")]
shuffle(deck)
for card in deck:
    print(f"{card[0]} of {card[1]}")