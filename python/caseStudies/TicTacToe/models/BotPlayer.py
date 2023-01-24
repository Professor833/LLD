from typing import *
from models.PlayerType import PlayerType
from models.Player import Player
from models.BotDifficultyLevel import BotDifficultyLevel


class BotPlayer(Player):
    def __init__(self, name: str, symbol: str, botDifficulty: BotDifficultyLevel):
        super().__init__(name, PlayerType.BOT, symbol)
        self.botDifficulty = botDifficulty
        self.botMoveStrategy = self.getBotMoveStrategy(botDifficulty)
