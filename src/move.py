from enum import Enum, auto

class Move(Enum):
    """Enums to distinguish and communicate the player's decisons.

    Enums:
        HIT: Ask for an additional card.
        STAND: Finish the hand.
        DBL: 'Double Down', doubles the wager and recieves 1 and only 1
              additional card.
        SPLIT: If your first two cards are identically valued, you may split
               them to form two seperate hands. A second bet, equal to your
               initial is automatically placed on your second hand. You may
               then proceed to draw cards as usual. However, if two Aces are
               split into seperate hands, you recieve only 1 additional card
               per hand. You may not resplit a hand that has already been split.
        BET: Play a new hand.
        QUIT: End simulation.

    """

    HIT = auto()
    STAND = auto()
    DBL = auto()
    SPLIT = auto()
    BET = auto()
    QUIT = auto()