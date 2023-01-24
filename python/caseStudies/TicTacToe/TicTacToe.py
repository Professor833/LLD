from typing import *
from models.Game import Game
from models.Player import Player
from models.HumanPlayer import HumanPlayer
from models.Cell import Cell
from models.Bot import Bot
from models.BotDifficultyLevel import BotDifficultyLevel
from controllers.GameController import GameController


class TicTacToe:
    def main(self) -> None:
        print('Welcome to Tic Tac Toe...')
        # totalPlayers = input("Enter total players: ")
        totalPlayers = 2

        # dimension = int(input("Enter dimensions: "))
        dimension = 3
        # isBotPlaying = True if input(
        #     "Is Bot Playing? (y/n): ") == 'y' else False
        isBotPlaying = False
        players = []
        toInterate = dimension - 1
        gameController = GameController()

        if isBotPlaying:
            toInterate = dimension - 2

        for i in range(toInterate):
            name = input(f"Enter Player {i + 1} name: ")
            symbol = input(f"Enter Player {i + 1} symbol: ")
            players.append(HumanPlayer(name, symbol))

        if isBotPlaying:
            botName = input(f"Enter Bot name: ")
            botSymbol = input(f"Enter Bot symbol: ")
            players.append(Bot(botName, botSymbol, BotDifficultyLevel.EASY))

        game: Game = gameController.createGame(dimension, players)

        game.start()

    def __init__(self) -> None:
        self.main()


if __name__ == '__main__':
    TicTacToe()
