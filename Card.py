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

    def card_strength(self):
        power_total = []
        __t = 1
        for r in Deck.RANK:
            power_total.append(__t)
            __t += 1
        return power_total

    def cards_to_suit(self, power_total):
        __couples = []
        card_deck = [[]]
        __v = 0
        __p = 0
        for rank in Deck.RANK:
            for suit in Deck.SUIT:
                for i in range(4):
                    card_deck[__p].append(rank + suit)
                    card_deck[__p].append(power_total[__v])
                    card_deck.append(__couples)
                    __couples = []
                    __p += 1
                    break
            __v += 1
        card_deck.pop()
        return card_deck

    def defining_a_trump_card(self, card_deck):
        trump = random.choice(card_deck)
        for card in trump:
            trump_suit = card[1]
            break
        trump_cards = []
        #if trump_suit == "0":
            #trump_suit = card[2]
        for card in card_deck:
            for c in card:
                if c[1] == trump_suit:
                    trump_cards.append(card)
                elif c[1] == "0" and c[2] == trump_suit:
                    trump_cards.append(card)
                break
        return trump_cards, trump, trump_suit

    def shuffle_the_deck(self, card_deck):
        random.shuffle(card_deck)
        return card_deck


class Player(object):
    def __init__(self, trump_cards):
        self.trump_cards = trump_cards

    def take_cards_from_the_deck(self, card_deck):
        self.cards = []
        if len(self.cards) < 6:
            for card in card_deck:
                self.cards.append(card)
                card_deck.remove(card)
        return self.cards


    def defining_trumps_in_hand(self):
        self.trump_cards
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

def main():
    deck = Deck()
    player = Player(deck.defining_a_trump_card(deck.cards_to_suit(deck.card_strength())))
    #print(deck.defining_a_trump_card(deck.cards_to_suit(deck.card_strength())),"\n")
    #print(deck.shuffle_the_deck(deck.cards_to_suit(deck.card_strength())))
    print(player.take_cards_from_the_deck(deck.cards_to_suit(deck.card_strength())))


main()
