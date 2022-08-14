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
            return True
        elif self.playerToken in self.board[0][0] and self.playerToken in self.board[1][1] and self.playerToken in self.board[2][2]:
            return True
        elif self.playerToken in self.board[0][2] and self.playerToken in self.board[1][1] and self.playerToken in self.board[2][0]:
            return True
        else:
            i = 0
            while i < 3:
                if self.playerToken in self.board[0][i] and self.playerToken in self.board[1][i] and self.playerToken in self.board[2][i]:
                    return True
                i += 1
        return False
    
    def searchComputerLine(self):
        if [self.computerToken, self.computerToken, self.computerToken] in self.board:
            return True
        elif self.computerToken in self.board[0][0] and self.computerToken in self.board[1][1] and self.computerToken in self.board[2][2]:
            return True
        elif self.computerToken in self.board[0][2] and self.computerToken in self.board[1][1] and self.computerToken in self.board[2][0]:
            return True
        else:
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
        raise ValueError("the values must be positive.")
    if [column, row] in playerMoves or [column, row] in computerMoves:
        clear()
    else:
        playerMoves += [[column, row]]
        board.putToken(column, row, board.playerToken)
        if board.searchPlayerLine() == True:
            clear()
            board.printBoard()
            win = input(termcolor.colored("You have won!", config["color"]["textColor"], attrs=["bold"]))
            clear()
            quit()
        while (randomMove in computerMoves or randomMove in playerMoves) and any("*" in sub for sub in board.board):
            randomMove = [np.random.randint(1, 4), np.random.randint(1, 4)]
        computerMoves += [randomMove]
        board.putToken(randomMove[0], randomMove[1], board.computerToken)
        if board.searchComputerLine() == True:
            clear()
            board.printBoard()
            lost = input(termcolor.colored("You have lost!", config["color"]["textColor"], attrs=["bold"]))
            clear()
            quit()
        if any("*" in sub for sub in board.board) == False:
            clear()
            board.printBoard()
            tie = input(termcolor.colored("There has been a ½ - ½ tie!", config["color"]["textColor"], attrs=["bold"]))
            clear()
            quit() 
        clear()