'''
Question: Write Low Level Design for Tic Tac Toe Game
'''


from typing import List


class TicTacToe:
    """A class representing a Tic Tac Toe game"""

    # define the game board as a list of strings
    board: List[str] = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print_board(self) -> None:
        """Prints the current state of the game board"""
        print("----------------")
        print("| " + self.board[0] + " | " +
              self.board[1] + " | " + self.board[2] + " |")
        print("----------------")
        print("| " + self.board[3] + " | " +
              self.board[4] + " | " + self.board[5] + " |")
        print("----------------")
        print("| " + self.board[6] + " | " +
              self.board[7] + " | " + self.board[8] + " |")
        print("----------------")

    def check_game_status(self) -> str:
        """
        Checks if the game is won, lost, or drawn and returns the result

        Returns:
            str: "X wins" if X wins, "O wins" if O wins, "draw" if the game is drawn,
                "not finished" if the game is not finished yet.
        """
        # check rows
        for i in range(3):
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] and self.board[i * 3] != " ":
                return self.board[i * 3] + " wins"
        # check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] and self.board[i] != " ":
                return self.board[i] + " wins"
        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != " ":
            return self.board[0] + " wins"
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != " ":
            return self.board[2] + " wins"
        # check if the game is drawn
        if " " not in self.board:
            return "draw"
        # if none of the above conditions are met, the game is not finished yet
        return "not finished"

    def update_board(self, player: str, position: int) -> bool:
        """
        Updates the game board with the player's move and returns whether the move was valid

        Args:
            player (str): the player who made the move ("X" or "O").
            position (int): the position on the board where the player wants to make the move.

        Returns:
            bool: True if the move was valid, False otherwise.
        """
        # check if the chosen position is valid
        if position < 0 or position >= 9:
            return False
        if self.board[position] != " ":
            return False
        # update the board with the player's move
        self.board[position] = player
        return True

    def play(self) -> None:
        '''
        Plays the game
        '''
        # print the empty game board
        self.print_board()
        # initialize the current player and the game status
        player = "X"
        game_status = "not finished"
        # keep playing until the game is finished
        while game_status == "not finished":
            # ask the current player to choose a position
            position = int(input("Choose a position for " + player + ": "))
            # update the board with the player's move
            if self.update_board(player, position):
                # print the updated game board
                self.print_board()
                # check if the game is finished
                game_status = self.check_game_status()
                # switch to the next player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("Invalid move")
        # print the game result
        print(game_status)


if __name__ == "__main__":
    game = TicTacToe()
    game.play()