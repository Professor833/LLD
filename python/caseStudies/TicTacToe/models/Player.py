from typing import *
from models.PlayerType import PlayerType
from models.Move import Move
from models.Board import Board
from models.Cell import Cell
from exceptions.AppException import AppException
from models.CellState import CellState


class Player:
    def __init__(self, name: str, playerType: PlayerType, symbol: str) -> None:
        self.__name = name
        self.__playerType = playerType
        self.__symbol = symbol

    # Getters
    def getName(self) -> str:
        return self.__name

    def getPlayerType(self) -> PlayerType:
        return self.__playerType

    def getSymbol(self) -> str:
        return self.__symbol

    def makeMove(self, board) -> Move:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        return Move(cell=Cell(row, col), player=self)
