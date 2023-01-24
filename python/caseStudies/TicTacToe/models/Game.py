from typing import *
from exceptions.AppException import AppException
from models.Player import Player
from models.Cell import Cell
from models.CellState import CellState
from models.GameStatus import GameStatus
from models.Move import Move
from models.Board import Board
from strategies.gameWinningStrategy import GameWinningStrategy
from strategies.OrderOneStrategy import OrderOneGameWinningStrategy


class Game:
    def __init__(self) -> None:
        self.__board: List[List[Cell]] = None
        self.__players: List[Player] = None
        self.__moves: List[Move] = None
        self.__gameStatus: GameStatus = GameStatus.IN_PROGRESS
        self.__nextPlayerIndex: int = 0
        self.__gameWinningStrategy: GameWinningStrategy = None
        self.__winner: Player = None

    # Getters
    def getBoard(self) -> List[List[Cell]]:
        return self.__board

    # def getPlayers(self) -> List[Player]:
    def getPlayers(self):
        return self.__players

    def getNextPlayerIndex(self) -> int:
        return self.__nextPlayerIndex

    def getGameStatus(self) -> GameStatus:
        return self.__gameStatus

    def getGameWinningStrategy(self) -> GameWinningStrategy:
        return self.__gameWinningStrategy

    def getWinner(self) -> Player:
        return self.__winner

    # Setters
    def setBoard(self, board: List[List[Cell]]) -> None:
        self.__board = board

    def setGameWinningStrategy(self, gameWinningStrategy: GameWinningStrategy) -> None:
        self.__gameWinningStrategy = gameWinningStrategy

    def setPlayers(self, players: List[Player]) -> None:
        if len(players) < 2 or len(players) > 2:
            raise AppException('Invalid totalPlayers')
        self.__players = players

    def setPlayerNextMoveIndex(self, playerNextMoveIndex: int) -> None:
        if playerNextMoveIndex < 0 or playerNextMoveIndex > 1:
            raise AppException('Invalid playerNextMoveIndex')
        self.__nextPlayerIndex = playerNextMoveIndex

    def setGameStatus(self, gameStatus: GameStatus) -> None:
        self.__gameStatus = gameStatus

    def setWinner(self, winner: Player) -> None:
        self.__winner = winner

    @staticmethod
    class GameBuilder:
        def __init__(self) -> None:
            self.dimension: int = 0
            self.players: List[Player] = None

        def setDimension(self, dimension: int) -> 'GameBuilder':
            self.dimension = dimension
            return self

        def setPlayers(self, players: List[Player]) -> 'GameBuilder':
            self.players = players.copy()
            return self

        def __validate_build(self) -> bool:
            pass

        def build(self) -> 'Game':
            self.__validate_build()
            game = Game()
            game.setBoard(Board(self.dimension))
            game.setPlayers(self.players)
            game.setGameWinningStrategy(OrderOneGameWinningStrategy(self.dimension)) # todo: make this configurable
            return game

    def __nextMove(self) -> None:
        toMovePlayer: Player = self.__players[self.__nextPlayerIndex]
        print('Player ', toMovePlayer.getName(), ' turn')
        move = toMovePlayer.makeMove(self.__board)

        row = move.getCell().getRow()
        col = move.getCell().getCol()
        # validate move
        if move is not None:
            if self.__board.getCell(row, col).getCellState() != CellState.FILLED:
                print('Invalid move')
                return

        print('Player ', toMovePlayer.getName(), ' move: ', row, col)
        self.__board[row][col].setCellState(CellState.FILLED)
        self.__board[row][col].setPlayer(toMovePlayer)
        self.__moves.append(move)

        # check if game is won
        if self.__gameWinningStrategy.checkWinner(self.__board, move):
            self.__gameStatus = GameStatus.ENDED
            self.__winner = toMovePlayer
            print('Player ', toMovePlayer.getName(), ' won!!')
            return

    def undo(self) -> None:
        pass

    def start(self) -> None:
        while self.getGameStatus() == GameStatus.IN_PROGRESS:
            print('Board: ', self.getBoard())
            self.__nextMove()

