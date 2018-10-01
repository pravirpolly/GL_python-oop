import random

__author__ = 'Endri Dani'

cards = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
card_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
               'K': 10}
global bankroll_amount, betting_amount


class Player(object):
    def __init__(self, bankroll=100):
        self.hand = []
        self.bankroll = bankroll

    def add_bankroll(self, amount):
        self.bankroll += amount

    def subtract_bankroll(self, amount):
        self.bankroll -= amount

    def initial_cards(self):
        first_card = random.choice(card_values.keys())
        second_card = random.choice(card_values.keys())
        self.hand.extend([first_card, second_card])
        print
        "Player: {}".format(self.hand)

    def add_card(self):
        card = random.choice(card_values.keys())
        self.hand.append(card)
        print
        "Player: {}".format(self.hand)

    def total_points(self):
        total = [card_values[item] for item in self.hand]
        return sum(total)


class Dealer(object):
    def __init__(self):
        self.hand = []

    def initial_card(self):
        first_card = random.choice(card_values.keys())
        self.hand.append(first_card)
        print
        "Dealer: {}".format(self.hand)

    def add_card(self):
        card = random.choice(card_values.keys())
        self.hand.append(card)
        print
        "Dealer: {}".format(self.hand)

    def total_points(self):
        total = [card_values[item] for item in self.hand]
        return sum(total)


def check_status():
    if player.total_points() > dealer.total_points() or dealer.total_points() > 21:
        print
        "You WIN!"
        player.add_bankroll(betting_amount)
        print
        "Your bankroll is {}".format(player.bankroll)
    elif player.total_points() < dealer.total_points():
        print
        "You LOSE!"
        player.subtract_bankroll(betting_amount)
        print
        "Your bankroll is {}".format(player.bankroll)
    elif player.total_points() == dealer.total_points():
        print
        "DRAW!"
        print
        "Your bankroll is {}".format(player.bankroll)


def check_initial_status():
    player.hand = []
    dealer.hand = []
    global more_cards
    more_cards = ''
    player.initial_cards()
    dealer.initial_card()
    while player.total_points() < 21:
        while not (more_cards == 'h' or more_cards == 's'):
            more_cards = raw_input("Do you want another card? (h/s): ")
        if more_cards == 'h':
            player.add_card()
            more_cards = ''
            print
            "Player Total: {}".format(player.total_points())
        elif more_cards == 's':
            print
            "Player: {}".format(player.hand)
            print
            "Player Total: {}".format(player.total_points())
            dealer.add_card()
            while dealer.total_points() <= 16:
                dealer.add_card()
                break
            print
            "Dealer Total: {}".format(dealer.total_points())
            check_status()
            break
    if player.total_points() == 21:
        player.add_bankroll(betting_amount)
        print
        "BlackJack"
        print
        "Your bankroll is {}".format(player.bankroll)
    elif player.total_points() > 21:
        player.subtract_bankroll(betting_amount)
        print
        "Busted"
        print
        "Your bankroll is {}".format(player.bankroll)


while True:
    try:
        bankroll_amount = int(raw_input("How much do you want to put in? :"))
    except ValueError:
        print
        "It looks like you did not enter a valid value!"
        continue
    else:
        player = Player(bankroll=bankroll_amount)
        dealer = Dealer()
        while player.bankroll > 0:
            try:
                betting_amount = int(raw_input("How much do you want to bet? :"))
            except ValueError:
                print
                "It looks like you did not enter a valid value!"
                continue
            if betting_amount > player.bankroll:
                print
                "Not enough money in the bankroll! Try again!"
            else:
                check_initial_status()
        else:
            print
            "No more money in your bankroll!\nThank You for playing!"
        break