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

RANK = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUIT = ["h", "t", "c", "s"]


def card_strength():
    t = 1
    power_total = []
    for r in RANK:
        power_total.append(t)
        t += 1
    return power_total


def cards_to_suit(power_total):
    couples = []
    v = 0
    p = 0
    card_deck = [[]]
    for rank in RANK:
        for suit in SUIT:
            for i in range(4):
                card_deck[p].append(rank + suit)
                card_deck[p].append(power_total[v])
                card_deck.append(couples)
                couples = []
                p += 1
                break
        v += 1
    card_deck.pop()
    return card_deck


def shuffle_the_deck(card_deck):
    random.shuffle(card_deck)
    return card_deck


def defining_a_trump_card(card_deck):
    trump = random.choice(card_deck)
    trump_cards = []
    for card in trump:
        trump_suit = card[1]
        break
    for card in card_deck:
        for c in card:
            if c[1] == trump_suit:
                trump_cards.append(card)
            elif c[1] == "0" and c[2] == trump_suit:
                trump_cards.append(card)
            break
    return trump_cards, trump, trump_suit


class Player(object):
    def __init__(self, trump_cards):
        self.trump_cards = trump_cards

    def take_cards_from_the_deck(self, card_deck):
        cards = []
        full_deck = False
        while not full_deck:
            if len(cards) < 6:
                for card in card_deck:
                    cards.append(card)
                    card_deck.remove(card)
                    break
            else:
                full_deck = True
        return cards

    def defining_trumps_in_hand(self, cards):
        my_trump = []
        for card in cards:
            for trump in self.trump_cards:
                for t in trump:
                    if card != t:
                        break
                    else:
                        my_trump.append(card)
                        break
        return my_trump

    def make_a_move(self, cards):
        card_on_the_table = None
        card_in_hand = False
        while not card_in_hand:
            chosen_card = input("Выбирете карту: ")
            for card in cards:
                for c in card:
                    if chosen_card != c:
                        break
                    else:
                        cards.remove(card)
                        card_on_the_table = card
                        card_in_hand = True
                        break
                if card_in_hand:
                    break
            if not card_in_hand:
                print("Нет такой карты")
            else:
                print("Вы положили карту на стол")
                return card_on_the_table


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
    player = Player(defining_a_trump_card(shuffle_the_deck(cards_to_suit(card_strength()))))
    print(player.defining_trumps_in_hand(player.take_cards_from_the_deck((shuffle_the_deck(cards_to_suit(card_strength()))))))
    player.make_a_move(player.take_cards_from_the_deck((shuffle_the_deck(cards_to_suit(card_strength())))))


main()
