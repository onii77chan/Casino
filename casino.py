from random import choice

deck = {
    '2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5, '6♠': 6, '7♠': 7, '8♠': 8, '9♠': 9, '10♠': 10, 'J♠': 10, 'Q♠': 10, 'K♠': 10, 'A♠': 11,
    '2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7, '8♥': 8, '9♥': 9, '10♥': 10, 'J♥': 10, 'Q♥': 10, 'K♥': 10, 'A♥': 11,
    '2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5, '6♦': 6, '7♦': 7, '8♦': 8, '9♦': 9, '10♦': 10, 'J♦': 10, 'Q♦': 10, 'K♦': 10, 'A♦': 11,
    '2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5, '6♣': 6, '7♣': 7, '8♣': 8, '9♣': 9, '10♣': 10, 'J♣': 10, 'Q♣': 10, 'K♣': 10, 'A♣': 11
}


class Casino:
    def __init__(self, bid, factor, cash, game_result=None):
        self.bid = bid
        self.factor = factor
        self.cash = cash
        self.game_result = game_result

    def bet(self):
        self.cash -= self.bid

    def bet_results(self, game_result):
        outcomes = {
            'win': self.bid * self.factor,
            'lose': -self.bid,
            'draw': self.bid,
        }
        if game_result not in outcomes:
            return 'Invalid data'

        self.cash += outcomes.get(game_result, 0)

    def __str__(self):
        return f"Bid: {self.bid}, Factor: {self.factor}"


class CardGame(Casino):
    def __init__(self, cash, bid, factor, card_deck=None, user_cards=None, used_cards=None):
        super().__init__(bid, factor, cash)
        if card_deck is None:
            self.card_deck = deck.copy()
        else:
            self.card_deck = card_deck
        if user_cards is None:
            self.user_cards = {}
        else:
            self.user_cards = user_cards
        if used_cards is None:
            self.used_cards = []
        else:
            self.used_cards = used_cards

    def get_new_card(self):
        while True:
            new_card = choice(self.card_deck)
            if new_card not in self.used_cards:
                self.used_cards.append(new_card)
                return new_card, self.user_cards.update(new_card.keys(), new_card.values())
            else:
                del [self.card_deck[new_card]]
                self.used_cards.append(new_card)

    def view_user_cards(self):
        return [card for card in self.user_cards]

    def view_user_cards_points(self):
        points = 0
        if self.user_cards:
            for point in self.user_cards.values():
                points += point
            return points
        else:
            return 0

    def __str__(self):
        return f"Bid: {self.bid}, Factor: {self.factor}"


