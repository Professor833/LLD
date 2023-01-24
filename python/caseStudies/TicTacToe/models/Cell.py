from typing import *
# from models.Player import Player
from models.CellState import CellState

class Cell:
    def __init__(self, row: int, col: int, player: 'Player' = None):
        self.__row = row
        self.__col = col
        self.__player = None
        self.__cellState = CellState.EMPTY;

    # Getters
    def getRow(self) -> int:
        return self.__row

    def getCol(self) -> int:
        return self.__col

    def getPlayer(self) -> 'Player':
        return self.__player

    def getCellState(self) -> CellState:
        return self.__cellState

    # Setters
    def setRow(self, row: int) -> None:
        self.__row = row

    def setCol(self, col: int) -> None:
        self.__col = col

    def setPlayer(self, player: 'Player') -> None:
        self.__player = player

    def setCellState(self, cellState: CellState) -> None:
        self.__cellState = cellState

    def __str__(self) -> str:
        temp = "Cell: (" + str(self.__row) + ", " + str(self.__col) + ") "
        if self.__player is not None:
            temp += "Player: " + str(self.__player.getSymbol())
        else:
            temp += "Player: None"

        return temp