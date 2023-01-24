from typing import *
from models.Cell import Cell


class Board:
    def __init__(self, size: int):
        self.size = size
        self.board: List[List[Cell]] = [
            [Cell(i, j) for i in range(size)]
            for j in range(size)
        ]

    # getters
    def getBoard(self) -> List[List[Cell]]:
        return self.board

    # utility methods
    def getCell(self, row: int, col: int) -> Cell:
        return self.board[row][col]

    def __str__(self) -> str:
        return str(self.board)