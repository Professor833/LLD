from typing import *
from abc import ABC, abstractmethod
from models.Cell import Cell
from models.Move import Move
from models.Player import Player


class BotMoveStrategy(ABC):
    @abstractmethod
    def makeMove(self, board: List[List[Cell]], player: Player) -> Move:
        pass
