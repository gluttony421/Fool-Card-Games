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
    RANG = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUIT = ["h", "t", "c", "s"]

    def defining_a_trump_card(self, cards):
        trump = random.choice(cards)
        trump_suit = trump[1]
        trump_cards = []
        if trump_suit == "0":
            trump_suit = trump[2]
        for card in cards:
            if card[1] == trump_suit:
                trump_cards.append(card)
            elif card[1] == "0" and card[2] == trump_suit:
                trump_cards.append(card)
        return trump_cards, trump, trump_suit

    def cards_to_suit(self):
        cards = []
        for rank in Deck.RANG:
            for suit in Deck.SUIT:
                cards.append(rank + suit)
        random.shuffle(cards)
        return cards



card = Deck()
print(card.cards_to_suit())
print(card.defining_a_trump_card(Deck.cards_to_suit(card)))


