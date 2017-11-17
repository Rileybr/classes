# Compare By Brandon Riley
# 11/16/17
# plays 5 rounds of the card game compare

import deck

new_deck = deck.Deck()
new_deck.shuffle()
new_deck.deal_card()


def compare_cards(player_one_card, player_two_card):
    """
    Checks who's card is higher, and if they are the same rank, then the suit is highest in alphabetical order
    :param player_one_card: the card of player one which is being compared
    :param player_two_card: the card of player two which is being compared
    :return: who won
    """
    print("-----------------------------------------------------------------------------------------------------------")
    print(player_one_card.rank, player_one_card.suit)
    print(player_two_card.rank, player_two_card.suit)
    # checks which card is higher in rank
    if player_one_card.rank > player_two_card.rank:
        print("player one won")
        return True
    elif player_two_card.rank > player_one_card.rank:
        print("player two won")
        return False
    elif player_one_card.rank == player_two_card.rank:
        # checks which card is higher in suit
        if player_one_card.suit > player_two_card.suit:
            print("player one won")
            return True
        elif player_two_card.suit > player_one_card.suit:
            print("player two won")
            return False


def play_game(player_one_card, player_two_card):
    """
    figures out the score and who won the game
    :param player_one_card: the cards of player one
    :param player_two_card: the cards of player two
    :return:
    """
    player_one_score = 0
    player_two_score = 0
    for x in range(5):  # compares the five different cards
        score = compare_cards(player_one_card[x], player_two_card[x])
        if score:
            player_one_score += 1
        else:
            player_two_score += 1
    print("-----------------------------------------------------------------------------------------------------------")
    if player_one_score > player_two_score:
        print("player one won the game")
    else:
        print("player two won the game")
    print("-----------------------------------------------------------------------------------------------------------")
    print("the final score was")
    print("player one:", player_one_score)
    print("player two:", player_two_score)


def main():
    new_deck.shuffle()
    player_one_card = []
    player_two_card = []
    for x in range(5):  # deals five cards to each player
        new_card = new_deck.deal_card()
        player_one_card.append(new_card)
        new_card = new_deck.deal_card()
        player_two_card.append(new_card)
    play_game(player_one_card, player_two_card)

main()
