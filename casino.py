from random import choice
import hashlib

deck = {
    '2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5, '6♠': 6, '7♠': 7, '8♠': 8, '9♠': 9, '10♠': 10, 'J♠': 10, 'Q♠': 10, 'K♠': 10, 'A♠': 11,
    '2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7, '8♥': 8, '9♥': 9, '10♥': 10, 'J♥': 10, 'Q♥': 10, 'K♥': 10, 'A♥': 11,
    '2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5, '6♦': 6, '7♦': 7, '8♦': 8, '9♦': 9, '10♦': 10, 'J♦': 10, 'Q♦': 10, 'K♦': 10, 'A♦': 11,
    '2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5, '6♣': 6, '7♣': 7, '8♣': 8, '9♣': 9, '10♣': 10, 'J♣': 10, 'Q♣': 10, 'K♣': 10, 'A♣': 11
}

separate_of_the_text = '_____________________________________________________________________'

access_list = {'user': 'BASIC', 'test': 'TESTER', 'admin': 'ADMINISTRATOR'}


def log_called_method_name(func):
    def wrapper(*args, **kwargs):
        print(f"{separate_of_the_text}\n"
              f"* Вызван метод: {func.__name__} *\n"
              f"{separate_of_the_text}\n")
        return func(*args, **kwargs)
    return wrapper


class AvailableCommands:
    def __init__(self, phase, access='user'):
        self.phase = phase
        self.access = access

    def create_available_commands(self):
        pass

    def create_actions_for_commands(self):
        pass


@log_called_method_name
def user_input(list_of_available_commands, ):
    while True:
        print(f"{separate_of_the_text}\n"
              "Список доступных команд:")

        for value_for_call_command, command_info in list_of_available_commands.items():
            print(f'{value_for_call_command}: {command_info}')
        user_input_data = input("Input: ")
        return user_input_data


class Access:
    def __init__(self, access: str):
        self.access = access

    def create_available_commands(self):
        hashpassword = hashlib.sha256(self.access.encode('utf-8')).hexdigest()
        return hashpassword


access = Access('admin')

q = access.create_available_commands()

inpute = Access(input('input: ')).create_available_commands()
if inpute == q:
    print('ok')
else:
    print('not ok')


class Casino:
    def __init__(self, bid, factor, cash, game_phase, game_result=None):
        self.bid = bid
        self.factor = factor
        self.cash = cash
        self.game_result = game_result
        self.game_phase = game_phase


    @log_called_method_name
    def bet(self):
        self.cash -= self.bid

    @log_called_method_name
    def bet_results(self, game_result):
        outcomes = {
            'win': self.bid * self.factor,
            'lose': -self.bid,
            'draw': self.bid,
        }
        if game_result not in outcomes:
            raise 'Invalid data in method bet_results'
        self.cash += outcomes.get(game_result, 0)

    @log_called_method_name
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

    @log_called_method_name
    def get_new_card(self):
        while True:
            new_card = choice(self.card_deck)
            if new_card not in self.used_cards:
                self.used_cards.append(new_card)
                return new_card, self.user_cards.update(new_card.keys(), new_card.values())
            else:
                del [self.card_deck[new_card]]
                self.used_cards.append(new_card)

    @log_called_method_name
    def view_user_cards(self):
        return [card for card in self.user_cards]

    @log_called_method_name
    def view_user_cards_points(self):
        points = 0
        if self.user_cards:
            for point in self.user_cards.values():
                points += point
            return points
        else:
            return 0

    @log_called_method_name
    def __str__(self):
        return f"Bid: {self.bid}, Factor: {self.factor}"
