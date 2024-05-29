from casino import (
    deck,
    CardGame,
    Casino,
    Dealer,
    Player,

)


class BlackJack(CardGame):
    def __init__(self, cash, bid, factor, card_deck, user_cards, used_cards):
        super().__init__(cash, bid, factor, card_deck, user_cards, used_cards)

    def surrender(self):
        """После раздачи первых двух карт на все играющие боксы игрок может отказаться от продолжения игры
        на любом количестве своих боксов, теряя при этом половину соответствующих ставок.
        Это возможно сделать до выхода третьей карты на бокс, на который хотят сделать SURRENDER.
        Игрок не может сделать SURRENDER, если первая карта дилера — туз.
        *Дилер не предлагает сорренда."""
        pass

    def split(self):
        """Если первые две карты игрока одного номинала, т. е. имеют одинаковое значение по очкам,
        то они могут быть разделены. При этом игрок делает дополнительную ставку на этом боксе,
        равную первоначальной, и набирает карты на каждую карту в отдельности.
        Все пары одинаковых карт могут быть разделены не более трех раз. Исключением являются тузы.
        Разделение тузов допускается дважды, и при разделении игрок получает только одну карту на каждый из тузов.
        Комбинация «туз и десять (картинка)», полученная после разделения,
        считается как 21 и не является комбинацией Блэкджек.На двух картах Сплита можно делать Дабл.
        На сплите Сорренда сделать нельзя."""
        pass

    def double(self):
        """После того, как игрок получил первые две карты, независимо от количества очков,
        он может удвоить свою ставку, получая при этом только одну карту (исключение составляют карты,
        образующие Блэк Джек). Разрешается удвоение после разделения карт. Если у игрока 9, 10 и 11 очков,
        то дилер всегда предложит игроку Дабл. Если игрок согласен,
        то он должен доставить фишки на сумму от минимума стола до суммы первоначальной ставки,
        за ставкой и объявить: «Дабл». По просьбе игрока дилер может сделать Дабл «втемную»,
        но только если количество очков на боксе не превышает 11."""
        pass

    def insurance(self):
        """Если первая карта дилера — туз, то дилер предлагает застраховать свой бокс от возможного у него Блэкджека.
        Любой игрок может сделать дополнительную ставку на Страховку, которая должна быть не меньше 5 у.е.
        и не больше максимальной ставки стола на каждый бокс. Эта ставка выигрывает, если у дилера выпадает Блэкджек,
        и оплачивается 2:1, во всех остальных случаях проигрывает.
        Блэк Джек застраховать нельзя."""
        pass