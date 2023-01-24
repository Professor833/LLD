from models.Cell import Cell


class Move:
    def __init__(self, cell: Cell, player: 'Player') -> None:
        self.__cell = cell
        self.__player = player

    # Getters
    def getCell(self) -> Cell:
        return self.__cell

    def getPlayer(self) -> 'Player':
        return self.__player

    # Setters
    def setCell(self, cell: Cell) -> None:
        self.__cell = cell

    def setPlayer(self, player: 'Player') -> None:
        self.__player = player
