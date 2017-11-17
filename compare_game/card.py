# Card By Brandon Riley
# 11/16/17
# creates a regular playing card


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def __str__(self):
        return str(self.rank) + self.suit
