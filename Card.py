'''
Карточная игра "Дурак"
1. В игре присутствует колода которая имеет список всех карт. Она передает карты игрокам в случае если у них на руках менее
6 карт. Если больше то игрок пропускает очередь на раздачу карт. Колода рандомным образом, среди всего списка карт,
определяет козырь. Таким же рандомным образом в начале каждой игры колода рандомно перемешивается.

2. Присутствуют два игрока. Определяется право первого хода от того какой наименьший козырь имеется на руках у игрока.
Ходы компьютера производятся от приоритета каждой карты, и взависимости от того какие в данный моменты карты имеются на
руках компьютера. В случае если в руке компьютера присутствуют карты с рангом схожие с теми что лежат на столе, то
компьютер подкидывает эту карту, так же в зависимости от приоритета подкидываемой карты.
Отбив карты игрока компьютером производится наименьшей из возможных вариантов имеющихся на руках.
В случае если масть и/или ранг имеющихся карт не способны перебить карту игрока, то компютер забирает их себе в руку.
(некоторые моменты схожие с игроком)

3. Карты. Карты могут иметь различный приоритет и ранг. Если карта имеет козырную масть то она имеет наивысший приоритет
и наибольшую силу.
'''

import random

class Deck(object):
    RANK = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUIT = ["h", "t", "c", "s"]

    def _defining_a_trump_card(self, power_in_cards):
        trump = random.choice(power_in_cards)
        trump_suit = trump[1]
        trump_cards = []
        if trump_suit == "0":
            trump_suit = trump[2]
        for card in power_in_cards:
            if card[1] == trump_suit:
                trump_cards.append(card)
            elif card[1] == "0" and card[2] == trump_suit:
                trump_cards.append(card)
        return trump_cards, trump, trump_suit

    def _cards_to_suit(self, power_total):
        __couples = []
        deck = [[]]
        __v = 0
        __p = 0
        for rank in Deck.RANK:
            for suit in Deck.SUIT:
                for i in range(4):
                    deck[__p].append(rank + suit)
                    deck[__p].append(power_total[__v])
                    deck.append(__couples)
                    __couples = []
                    __p += 1
                    break
            __v += 1
        deck.pop()
        random.shuffle(deck)
        return deck

    def _card_strength(self):
        power_total = []
        __t = 1
        for r in Deck.RANK:
            power_total.append(__t)
            __t += 1
        return power_total



class Player(object):
    def __init__(self, cards, trump_cards):
        self.cards = cards
        self.trump_cards = trump_cards

    def take_cards_from_the_deck(self):
        pass

    def make_a_move(self):
        pass

    def throw_a_card(self):
        pass

    def take_a_card_from_the_table(self):
        pass


class Table(object):
    def take_player_cards(self):
        pass

    def give_cards_to_a_player(self):
        pass

    def hang_up(self):
        pass

card = Deck()
print(card._cards_to_suit(card._card_strength()))
#print(card.defining_a_trump_card(card.cards_to_suit(card.card_strength())))


