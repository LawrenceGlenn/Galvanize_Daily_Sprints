import random

def make_deck():
    deck = []
    for x in range(3):
        deck.append("s")
        deck.append("d")
    for x in range(44):
        deck.append("n")

def make_hand():
    hand = []
    for x in range(5):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)

count = 0
for x in range 100:
    make_deck()
    make_hand()
    while("s" in hand):
        hand.remove("s")
        for x in range 3:
            card = random.choice(deck)
            hand.append(card)
            deck.remove(card)

    if  "d" in hand:
        count += 1
print(count)
