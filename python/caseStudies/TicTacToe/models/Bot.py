from models.Player import Player
from models.BotDifficultyLevel import BotDifficultyLevel

class Bot:
    def __init__(self, name: str, symbol: str, difiicultyLevel: BotDifficultyLevel) -> None:
        self.name = name
        self.symbol = symbol
        self.difiicultyLevel = difiicultyLevel
