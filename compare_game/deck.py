# Deck By Brandon Riley
# 11/16/17
# Creates a deck, shuffles it, and deals a random card

import card
import random


class Deck:
    def __init__(self):
        self.deck_list = []
        for suits in ["c", "h", "s", "d"]:
            for x in range(1, 14):
                new_card = card.Card(x, suits)
                self.deck_list.append(new_card)

    def shuffle(self):
        random.shuffle(self.deck_list)

    def deal_card(self):
        return self.deck_list.pop(0)
