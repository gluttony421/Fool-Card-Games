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


class Deck(object):
    def __init__(self, power_total=[], card_deck=[[]], trump_cards=[], trump=None, trump_suit=None):
        self.power_total = power_total
        self.card_deck = card_deck
        self.trump_cards = trump_cards
        self.trump = trump
        self.trump_suit = trump_suit

    def card_strength(self):
        t = 1
        for r in RANK:
            self.power_total.append(t)
            t += 1

    def cards_to_suit(self):
        couples = []
        v = 0
        p = 0
        for rank in RANK:
            for suit in SUIT:
                for i in range(4):
                    self.card_deck[p].append(rank + suit)
                    self.card_deck[p].append(self.power_total[v])
                    self.card_deck.append(couples)
                    couples = []
                    p += 1
                    break
            v += 1
        self.card_deck.pop()

    def shuffle_the_deck(self):
        random.shuffle(self.card_deck)

    def defining_a_trump_card(self):
        self.trump = random.choice(self.card_deck[15:])
        for card in self.trump:
            if card[1] == "0":
                self.trump_suit = card[2]
            else:
                self.trump_suit = card[1]
            break
        for card in self.card_deck:
            for c in card:
                if c[1] == self.trump_suit:
                    self.trump_cards.append(card)
                elif c[1] == "0" and c[2] == self.trump_suit:
                    self.trump_cards.append(card)
                break

    def trump_card_strength(self):
        for strength_trump in self.trump_cards:
            for i in strength_trump:
                if type(i) is int:
                    strength_trump.remove(i)
                    i += 10
                    strength_trump.append(i)


class Player(object):
    def __init__(self, trump_cards, turn, cards=[], cards_on_the_table=[], beat_cards=[]):
        self.trump_cards = trump_cards
        self.turn = turn
        self.cards_on_the_table = cards_on_the_table
        self.cards = cards
        self.beat_cards = beat_cards

    def take_cards_from_the_deck(self, card_deck):
        full_deck = False
        while not full_deck:
            if len(self.cards) < 6:
                for card in card_deck:
                    self.cards.append(card)
                    card_deck.remove(card)
                    break
            else:
                full_deck = True

    def make_a_move(self):
        if self.turn:
            while self.turn:
                chosen_card = input("Выбирете карту: ")
                for card in self.cards:
                    for c in card:
                        if chosen_card != c:
                            break
                        else:
                            self.cards.remove(card)
                            self.cards_on_the_table.append(card)
                            self.turn = False
                            break
                    if not self.turn:
                        break
                if self.turn:
                    print("Нет такой карты")
                else:
                    print("Вы положили карту на стол")
#не принимает 10
    def beating(self):
        self.turn = True
        if self.turn:
            if len(self.cards_on_the_table) != 0:
                while self.turn:
                    chosen_card = input("Выбирете карту: ")
                    for card in self.cards:
                        for t in card[:1]:
                            if chosen_card != t:
                                break
                            else:
                                for card_table in self.cards_on_the_table:
                                    for c in card[1:]:
                                        for n in card_table[:1]:
                                            print(c)
                                            if c > 10:
                                                print("Вы ходите козырем")
                                                if card[1:] > card_table[1:]:
                                                    self.cards.remove(card)
                                                    self.beat_cards.append(card)
                                                    print("Вы бьёте карту")
                                                    self.turn = False
                                                else:
                                                    print("Вы не бьёте карту")
                                            elif t[1:] != n[1:]:
                                                for tc in t[0]:
                                                    if tc == "1":
                                                        if t[2] != n[1:]:
                                                            print("Масть не совпадает")
                                                        elif card[1:] > card_table[1:] and t[2] == n[1:]:
                                                            self.cards.remove(card)
                                                            self.beat_cards.append(card)
                                                            print("Вы бьёте карту")
                                                            self.turn = False
                                                        else:
                                                            print("Карта слишком мала")
                                            else:
                                                print("Масть совпадает")
                                                if card[1:] > card_table[1:] and t[1:] == n[1:]:
                                                    self.cards.remove(card)
                                                    self.beat_cards.append(card)
                                                    print("Вы бьёте карту")
                                                    self.turn = False
                                                else:
                                                    print("Вы не бьёте карту")
                    if self.turn:
                        print("Выберите другую карту")


    def throw_a_card(self):
        flag = False
        for card_on_the_table in self.cards_on_the_table:
            for card_rank_on_the_table in card_on_the_table[0]:
                if flag:
                    break
                for i in card_rank_on_the_table[0]:
                    if flag:
                        break
                    if i == "1":
                        i = "10"
                    for card in self.cards:
                        if flag:
                            break
                        for c in card[0]:
                            if c == "1":
                                c = "10"

                            if i != c:
                                break
                            else:
                                flag = True
                                break
                break
        if flag:
            print("Вы можете подкинуть карту")
        else:
            print("Вам нечего подкинуть")

    def take_a_card_from_the_table(self):
        desire_to_take = input("Вы хотите забрать?: ")
        if desire_to_take == "да":
            for card_on_the_table in self.cards_on_the_table:
                self.cards.append(card_on_the_table)
                self.cards_on_the_table.remove(card_on_the_table)


class Enemy(Player):
    def __init__(self, trump_cards, turn, cards=[], cards_on_the_table=[]):
        super().__init__(trump_cards, turn, cards=[], cards_on_the_table=[])

    def make_a_move(self):
        strength = []
        for card in self.cards:
            for c in card[1:]:
                strength.append(c)
        minimum_strength = strength.index(min(strength))
        minimum_volue = self.cards[minimum_strength]
        self.cards.remove(minimum_volue)
        self.cards_on_the_table.append(minimum_volue)

    def throw_a_card(self):
        pass

    def take_a_card_from_the_table(self):
        pass


def main():
    turn = True
    deck = Deck()
    player = Player(deck.trump_cards, turn)
    enemy = Enemy(deck.trump_cards, turn)
    deck.card_strength()
    deck.cards_to_suit()
    deck.shuffle_the_deck()
    deck.defining_a_trump_card()
    deck.trump_card_strength()

    #print(deck.card_deck)
    #print(deck.trump_cards)
    #print(deck.trump_suit)
    print(deck.trump)
    player.take_cards_from_the_deck(deck.card_deck)
    print(player.cards)
    player.make_a_move()
    player.beating()
    #enemy.take_cards_from_the_deck(deck.card_deck)
   # print(enemy.cards)
    #enemy.make_a_move()
    #print(enemy.cards_on_the_table)
   # print(enemy.cards)




main()
