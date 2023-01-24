from typing import *
from models.PlayerType import PlayerType
from models.Player import Player

class HumanPlayer(Player):
    def __init__(self, name: str, symbol: str, ):
        super().__init__(name, PlayerType.HUMAN, symbol)