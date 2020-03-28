import random


class Card:
    'Clasa de baza pentru carti de joc'

    def __init__(self, value, colour):
        self.value = value
        self.colour = colour

    def peek(self):
        print("{} de {}".format(self.value, self.colour))


check = 0


class Deck:
    card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    card_colour = ["Inima_rosie", "Inima_neagra", "Romb", "Trefla"]


    def __init__(self):
        self.cards = []
        self.collect_cards()

    def collect_cards(self):

        for v in self.card_value:
            for c in self.card_colour:
                self.cards.append(Card(v, c))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def unpack(self):
        for card in self.cards:
            print("{} de {}".format(card.value, card.colour))
        print(len(self.cards))

    def validate_card(self, value, colour):
        if colour not in self.card_colour or value not in self.card_value:
            return False
        else:
            return True

    def remove_card(self, value, colour):
        if not self.validate_card(value, colour):
            print("nu exista acest tip de carte ({} de {})".format(value, colour))
        if len(self.cards) > 0:
            for card in self.cards:
                if card.value != value or card.colour != colour:
                    # print("Cartea {} de {} nu exista in pachet".format(card.value, card.colour))
                    continue
                else:
                    self.cards.remove(card)
                    print("Cartea {} de {} a fost eliminata".format(card.value, card.colour))
                    break
        else:
            print("pachetul este gol")

    def check_card(self, value, colour):
        global check
        card = Card(value, colour)
        if len(self.cards) <= 52:
            for i in self.cards:
                if i.colour == card.colour and i.value == card.value:
                    check = False
                    break
                else:
                    check = True

    def add_card(self, value, colour):
        card = Card(value, colour)
        self.check_card(value, colour)
        if not self.validate_card(value, colour):
            print("Cartea {} de {} nu exista".format(value, colour))
        elif check:
            self.cards.append(card)
            print("Cartea {} de {} a fost adaugata".format(value, colour))
        else:
            print("Cartea {} de {} exista deja in pachet".format(value, colour))


if __name__ == "__main__":
    deck = Deck()
    # deck.shuffle()
    deck.unpack()
    deck.remove_card("3", "Trefla")
    deck.remove_card("A", "Romb")
    deck.remove_card("5", "Romb")
    deck.remove_card("2", "Trefla")
    deck.add_card("2", "Inima_neagra")
    deck.add_card("A", "Romb")
    deck.add_card("8", "Inime_rosie")
    deck.unpack()

