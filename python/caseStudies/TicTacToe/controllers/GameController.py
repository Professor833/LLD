from models.Game import Game
from typing import *
from models.Player import Player


class GameController:

    def undo(self, game: Game) -> None:
        game.undo()

    def createGame(self, dimension: int, players: List[Player]) -> Game:
        try:
            return Game.GameBuilder().setDimension(dimension).setPlayers(players).build()
        except Exception as e:
            raise e


    def start(self, game: Game) -> None:
        game.start()

    def getGameStatus(self, game: Game) -> str:
        return game.getGameStatus()
