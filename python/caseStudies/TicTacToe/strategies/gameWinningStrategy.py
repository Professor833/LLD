from models.Board import Board
from models.Move import Move
from abc import ABC, abstractmethod


class GameWinningStrategy(ABC):
    @abstractmethod
    def checkWinner(self, board: Board, move: Move) -> bool:
        pass