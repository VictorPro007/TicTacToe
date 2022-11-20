"""
This Python project (https://github.com/VictorPro007/TicTacToe) is a Tic-Tac-Toe game created by VictorPro007 (https://github.com/VictorPro007).
To report bugs or errors, go to the GitHub issues page (https://github.com/VictorPro007/TicTacToe/issues).
You can configurate the game with the config.yml file.
Requirements:
  - Pyfiglet (https://pypi.org/project/pyfiglet/).
  - Termcolor (https://pypi.org/project/termcolor/).
  - NumPy (https://pypi.org/project/numpy/).
  - PyYAML (https://pypi.org/project/PyYAML/).
"""

import os
import pyfiglet
import termcolor 
import numpy as np
import yaml

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

class GameBoard:
    def __init__(self):
        self.board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        self.playerToken = config["token"]["playerToken"]
        self.computerToken = config["token"]["computerToken"]

    def putToken(self, column: int, row: int, token: str):
        self.board[row - 1][column - 1] = token

    def searchPlayerLine(self):
        if [self.playerToken, self.playerToken, self.playerToken] in self.board:
            # Check for horizontal lines.
            return True
        elif self.playerToken in self.board[0][0] and self.playerToken in self.board[1][1] and self.playerToken in self.board[2][2]:
            # Check for diagonal lines.
            return True
        elif self.playerToken in self.board[0][2] and self.playerToken in self.board[1][1] and self.playerToken in self.board[2][0]:
            # Check for diagonal lines.
            return True
        else:
            # Check for vertical lines.
            i = 0
            while i < 3:
                if self.playerToken in self.board[0][i] and self.playerToken in self.board[1][i] and self.playerToken in self.board[2][i]:
                    return True
                i += 1
        return False
    
    def searchComputerLine(self):
        if [self.computerToken, self.computerToken, self.computerToken] in self.board:
            # Check for horizontal lines.
            return True
        elif self.computerToken in self.board[0][0] and self.computerToken in self.board[1][1] and self.computerToken in self.board[2][2]:
            # Check for diagonal lines.
            return True
        elif self.computerToken in self.board[0][2] and self.computerToken in self.board[1][1] and self.computerToken in self.board[2][0]:
            # Check for diagonal lines.
            return True
        else:
            # Check for vertical lines.
            i = 0
            while i < 3:
                if self.computerToken in self.board[0][i] and self.computerToken in self.board[1][i] and self.computerToken in self.board[2][i]:
                    return True
                i += 1
        return False  

    def printBoard(self):
        for e in self.board:
            for se in e:
                if se == self.playerToken:
                    print(termcolor.colored(self.playerToken, config["color"]["playerColor"], attrs=["bold"]) + " "*10, end=" ")
                elif se == self.computerToken:
                    print(termcolor.colored(self.computerToken, config["color"]["computerColor"], attrs=["bold"]) + " "*10, end=" ")
                else: 
                    print(se + " "*10, end=" ")
            print("\n"*3)
        print(termcolor.colored("Player: ", config["color"]["textColor"], attrs=["bold"]) + termcolor.colored(self.playerToken, config["color"]["playerColor"], attrs=["bold"]))
        print(termcolor.colored("Computer: ", config["color"]["textColor"], attrs=["bold"]) + termcolor.colored(self.computerToken, config["color"]["computerColor"], attrs=["bold"]))

board = GameBoard()
playerMoves = []
computerMoves = []
randomMove = [np.random.randint(1, 4), np.random.randint(1, 4)]
clear()
pyfiglet.print_figlet("Tic    - Tac    - Toe", "big", config["color"]["titleColor"])
enter = input(termcolor.colored("PRESS ENTER TO PLAY THE GAME", config["color"]["textColor"], attrs=["bold"]))
clear()
while True:
    board.printBoard()
    column = int(input(termcolor.colored("Column: ", config["color"]["textColor"], attrs=["bold"])))
    row = int(input(termcolor.colored("Row: ", config["color"]["textColor"], attrs=["bold"])))
    if column <= 0 or row <= 0:
        clear()
    elif column > 3 or row > 3:
        clear()
    elif [column, row] in playerMoves or [column, row] in computerMoves:
        clear()
    else:
        playerMoves += [[column, row]]
        board.putToken(column, row, board.playerToken)
        if board.searchPlayerLine() == True:
            # If there is a player-generated line on the board, the player has won.
            clear()
            board.printBoard()
            win = input(termcolor.colored("You have won!", config["color"]["textColor"], attrs=["bold"]))
            clear()
            quit()
        while (randomMove in computerMoves or randomMove in playerMoves) and any("*" in sub for sub in board.board):
            # While randomMove is in either computerMoves or playerMoves and there is at least one asterisk on the board, reassign the randomMove variable.
            randomMove = [np.random.randint(1, 4), np.random.randint(1, 4)]
        computerMoves += [randomMove]
        board.putToken(randomMove[0], randomMove[1], board.computerToken)
        if board.searchComputerLine() == True:
            # If there is a computer-generated line on the board, the player has lost.
            clear()
            board.printBoard()
            lost = input(termcolor.colored("You have lost!", config["color"]["textColor"], attrs=["bold"]))
            clear()
            quit()
        if any("*" in sub for sub in board.board) == False:
            # If there is no asterisk or line on the board, there has been a draw. 
            clear()
            board.printBoard()
            draw = input(termcolor.colored("There has been a draw!", config["color"]["textColor"], attrs=["bold"]))
            clear()
            quit() 
        clear()
