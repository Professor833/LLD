from strategies.gameWinningStrategy import GameWinningStrategy
from models.Board import Board
from models.Move import Move
from typing import List, Dict


class OrderOneGameWinningStrategy(GameWinningStrategy):

    def __init__(self, dimension: int) -> None:
        self.rowSymbolCounts: List[Dict[str, int]] = []
        self.colSymbolCounts: List[Dict[str, int]] = []
        self.topLeftDiagSymbolCounts: Dict[str, int] = {}
        self.topRightDiagSymbolCounts: Dict[str, int] = {}

        for i in range(dimension):
            self.rowSymbolCounts.append({})
            self.colSymbolCounts.append({})

    def isCellOnTopLeftDiag(self, row: int, col: int) -> bool:
        return row == col

    def isCellOnTopRightDiag(self, row: int, col: int, dimension: int) -> bool:
        return row + col == dimension - 1

    def checkWinner(self, board: Board, move: Move) -> bool:
        symbol = move.getPlayer().getSymbol()
        row = move.getRow()
        col = move.getCol()
        dimension = board.getBoard().size()

        if symbol not in self.rowSymbolCounts[row]:
            self.rowSymbolCounts[row][symbol] = 0

        self.rowSymbolCounts[row][symbol] += 1

        if symbol not in self.colSymbolCounts[col]:
            self.colSymbolCounts[col][symbol] = 0

        self.colSymbolCounts[col][symbol] += 1

        if self.isCellOnTopLeftDiag(row, col):
            if symbol not in self.topLeftDiagSymbolCounts:
                self.topLeftDiagSymbolCounts[symbol] = 0
            self.topLeftDiagSymbolCounts[symbol] += 1

        if self.isCellOnTopRightDiag(row, col, dimension):
            if symbol not in self.topRightDiagSymbolCounts:
                self.topRightDiagSymbolCounts[symbol] = 0
            self.topRightDiagSymbolCounts[symbol] += 1

        if self.rowSymbolCounts[row][symbol] == dimension or self.colSymbolCounts[col][symbol] == dimension:
            return True

        if self.isCellOnTopRightDiag(row, col, dimension) and self.topRightDiagSymbolCounts[symbol] == dimension:
            return True

        if self.isCellOnTopLeftDiag(row, col) and self.topLeftDiagSymbolCounts[symbol] == dimension:
            return True

        return False
