class Hand:
    """Represents a hand of cards and their associated wager.

    Attributes:
        cards: a list of chars representing the cards in the hand.
               possible cards are A,2,3,4,5,6,7,8,9,X. These limitations of
               the possible chars are not enforced, care must be used when
               setting.
        bet: the value of the bet placed on the hand.
        is_split: a boolean that is true iff the hand was a result of a split.
        is_split_aces: a boolean that is true iff the hand was a result of
            splitting aces.

    """

    def __init__(self, hand, bet, is_split, is_split_aces):
        """initialize a new hand with 2 cards and a wager(bet).

        Args:
            hand(list of char): a list of two chars representing
                the initial two cards of a Blackjack hand.
            bet(int): the value of the initial bet on this hand.
            is_split(bool): true iff the hand was a result of a split.
            is_split_aces(bool): true iff the hand was a result of split aces.

        """
        self.hand = hand
        self.bet = bet
        self.is_split = is_split
        self.is_split_aces = is_split_aces

    def add_card(self, card):
        """add a card to the hand.

        Args:
            card(char): a char representing the value of the card added.
        """
        self.hand.append(card)

    def double_down(self, card):
        """add a card to the hand and doubles the bet.

        In Blackjack, after a double down move is played, no additional cards
        may be added to the hand after the double down card. However, this
        function does not enforce this behavior.

        Args:
            card(char): a char representing the value of the card added.
        """
        self.add_card(card)
        self.bet *= 2

    def get_value(self):
        """return the value of the hand."""
        result = 0
        num_aces = 0
        for card in hand:
            if card.isdigit():
                result += int(str)
            elif card == "X":
                result += 10
            elif card == "A":
                result += 11
                num_aces += 1
            else:
                #Something went wrong
                raise ValueError("Illegal Card")
