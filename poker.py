import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r)) #crea el palo con sus respectivos palos.

    def shuffle(self):
        random.shuffle(self.cards) # que se baraje

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one()) #reparte 5

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand #que salio en la mano

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True # ve si hay un par
        return False
#
    def two_pair(self):
        pairs = 0
        for i in range(5):
            for j in range(i+ 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    pairs += 1
        if pairs == 2:
            return True
        return False

    def three (self):
        for i in range(5):
            for j in range(i+ 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    for t in range(j + 1, 5):
                        if self.cards[i].get_rank() ==self.cards[t].get_rank():
                            return True
        return False

    def flush(self):

        suit = self.cards[0].get_suit()
        for i in range(1, 5):
            if suit != self.cards[i].get_suit():
                return False

        return True

    def is_full_house(self):

        ful = self.cards.copy()
        ful.sort()

        # dont know what to do next

    def four(self):
        for i in range(5):
            for j in range(i + 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    for t in range(j + 1, 5):
                        if self.cards[i].get_rank() == self.cards[t].get_rank():
                            for m in range(t + 1, 5):
                                if self.cards[m].get_rank() == self.cards[m].get_rank():
                                    return True
        return False




new_deck = Deck()
new_deck.shuffle()
print(new_deck)
hand = Hand(new_deck)
print(hand)
