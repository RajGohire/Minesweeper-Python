from Moves import getNeighbourMines, isValidMove
from colorama import Fore, Back, Style
from random import randrange
from tkinter import *

class GameBoard():
    def __init__(self, parent):
        return

    def updateBoard(self, game, x, y):
        if ([x, y] in game.mines):
            game.btns[x][y].config(text = '*', bg = "RED", fg = "WHITE", font = (15))
            game.gameOver = True
        else:
            count = getNeighbourMines(game, x, y)
            if (count != 0):    game.btns[x][y].config(text = count, bg = "GREEN")
            else:               game.btns[x][y].config(text = ' ', bg = "GREEN"); self.expandBoard(game, x, y)

    def expandBoard(self, game, x, y):
        if (x != 0 and game.btns[x-1][y]["text"] == '' and                                      [x-1, y] not in game.mines):    self.updateBoard(game, x-1, y)
        if (x != game.size-1 and game.btns[x+1][y]["text"] == '' and                            [x+1, y] not in game.mines):    self.updateBoard(game, x+1, y)
        if (y != 0 and game.btns[x][y-1]["text"] == '' and                                      [x, y-1] not in game.mines):    self.updateBoard(game, x, y-1)
        if (y != game.size-1 and game.btns[x][y+1]["text"] == '' and                            [x, y+1] not in game.mines):    self.updateBoard(game, x, y+1)
        if (x != 0 and y != 0 and game.btns[x-1][y-1]["text"] == '' and                         [x-1, y-1] not in game.mines):  self.updateBoard(game, x-1, y-1)
        if (x != game.size-1 and y != 0 and game.btns[x+1][y-1]["text"] == '' and               [x+1, y-1] not in game.mines):  self.updateBoard(game, x+1, y-1)
        if (x != 0 and y != game.size-1 and game.btns[x-1][y+1]["text"] == '' and               [x-1, y+1] not in game.mines):  self.updateBoard(game, x-1, y+1)
        if (x != game.size-1 and y != game.size-1 and game.btns[x+1][y+1]["text"] == '' and     [x+1, y+1] not in game.mines):  self.updateBoard(game, x+1, y+1)

    def buttonClicked(self, game, btn, x, y):
        game.x, game.y = x, y
        # print(x, y, game.x, game.y)
        self.updateBoard(game, x, y)

    def newBoard(self, parent, game):
        btns = []
        for x in range(game.size):
            btns.append([])
            for y in range(game.size):
                self.xy = Frame(parent, height = 40, width = 90)
                self.xyb = Button(self.xy, text = '', height = 40//game.size, width = 90//game.size, bg = "Grey", font = (15))
                self.xyb["command"] = lambda row=x, column=y, btn = self.xyb : self.buttonClicked(game, btn, row, column)
                self.xyb.grid(column = y, row = x)
                self.xy.columnconfigure(0, weight = 1)
                self.xy.rowconfigure(0, weight=1)
                self.xy.grid(column = y, row = x)
                self.xyb.grid(sticky="wens")
                self.xyb.pack()
                btns[x].append(self.xyb)
        game.btns = btns
        frame = Frame(parent)
        new = Button(frame, text = "Quit Game", height = 2, bg = "RED", fg = "WHITE", command = self.close)
        frame.grid(row = game.size+1, column = 0, columnspan = game.size, sticky = W+E)
        new.pack()
    
    def close(self):
        print("################# Game Over! #################\n")
        quit()

def newBoard(size):
    board = [['' for i in range(size+1)] for j in range(size)]
    return board

def plantMines(game):
    count = 0
    if (game.numMines == 0):
        game.numMines = randrange(1,15)
    while (count < game.numMines):
        x = randrange(0,game.size)
        y = randrange(0,game.size)
        while ([x,y] in game.mines):
            x = randrange(0,game.size)
            y = randrange(0,game.size)
        # game.board[x][y] = '*'
        game.mines.append([x, y])
        count += 1
    game.mines.sort()

def printBoard(size, board):
    print("\n---------------------------------------------")
    print("    " + str("   {}  "*size).format(*range(1,size+1)) + "\n" \
        + "    " + "+-----"*size + "+")
    for x in range (size):
        print(" " + chr(97 + x), end="  |")
        for y in range (size):
            if (board[x][y] == ''):
                print(f'{Back.LIGHTMAGENTA_EX}     {Style.RESET_ALL}|', end = "")
                continue
            elif (board[x][y] == '*'):
                print(f'{Back.RED}  {board[x][y]}  {Style.RESET_ALL}|', end = "")
                continue
            else:
                print(f'{Back.LIGHTGREEN_EX}{Fore.BLACK}  {board[x][y]}  {Style.RESET_ALL}|', end = "")
                continue
        print("\n    " + "+-----"*size + "+")
    print()

def updateBoard(game, x, y):
    if ([x, y] in game.mines):
        game.board[x][y] = '*'
        game.gameOver = True
    else:
        count = getNeighbourMines(game, x, y)
        if (count != 0):    game.board[x][y] = count
        else:               game.board[x][y] = ' '; expandBoard(game, x, y)

def expandBoard(game, x, y):
    print(x, y)
    if (x != 0 and game.board[x-1][y] == '' and                                     [x-1, y] not in game.mines):    updateBoard(game, x-1, y)
    if (x != game.size-1 and game.board[x+1][y] == '' and                           [x+1, y] not in game.mines):    updateBoard(game, x+1, y)
    if (y != 0 and game.board[x][y-1] == '' and                                     [x, y-1] not in game.mines):    updateBoard(game, x, y-1)
    if (y != game.size-1 and game.board[x][y+1] == '' and                           [x, y+1] not in game.mines):    updateBoard(game, x, y+1)
    if (x != 0 and y != 0 and game.board[x-1][y-1] == '' and                        [x-1, y-1] not in game.mines):  updateBoard(game, x-1, y-1)
    if (x != game.size-1 and y != 0 and game.board[x+1][y-1] == '' and              [x+1, y-1] not in game.mines):  updateBoard(game, x+1, y-1)
    if (x != 0 and y != game.size-1 and game.board[x-1][y+1] == '' and              [x-1, y+1] not in game.mines):  updateBoard(game, x-1, y+1)
    if (x != game.size-1 and y != game.size-1 and game.board[x+1][y+1] == '' and    [x+1, y+1] not in game.mines):  updateBoard(game, x+1, y+1)

def printGame(game):
    print("\n---------------------------------------------")
    print("{} player's turn!".format(game.turn))
    print("---------------------------------------------\n" \
        + "    +----+----+----+----+----+----+----+----+")
    for x in range (8,0,-1):
        print(x, end = "   | ")
        for y in range (1,9):
            if (game.board[x][y] == ''):
                if (game.checkers and abs(x-y) % 2 == 0):
                    print(f'{Back.LIGHTBLACK_EX}  {Style.RESET_ALL}' + ' | ', end = "")
                else:
                    print('   | ', end = "")
                continue
            if (game.board[x][y].isupper()):
                if (game.checkers and abs(x-y) % 2 == 0):
                    print(f'{Fore.GREEN}{Back.LIGHTBLACK_EX}{game.board[x][y]}{Style.RESET_ALL} | ', end = "")
                else:
                    print(f'{Fore.GREEN}{game.board[x][y]}{Style.RESET_ALL} | ', end = "")
            else:
                if (game.checkers and abs(x-y) % 2 == 0):
                    print(f'{Fore.RED}{Back.LIGHTBLACK_EX}{game.board[x][y]}{Style.RESET_ALL} | ', end = "")
                else:
                    print(f'{Fore.RED}{game.board[x][y]}{Style.RESET_ALL} | ', end = "")
        print("\n    +----+----+----+----+----+----+----+----+")
    print()

    for j in range (8):
        if (j == 0):
            print("{0:6s}".format(""), end="")
        print(chr(97 + j), end="{:4s}".format(""))  # Use ord() for char to int
    print("\n")

def updateGame(game):
    if (game.board[game.fy][game.fx].lower().strip() == 'k'):
        game.gameOver = True
    game.board[game.fy][game.fx] = game.board[game.oy][game.ox]
    game.board[game.oy][game.ox] = ''
    
    # Pawn Promotion
    if (game.fy == 8 and game.board[game.fy][game.fx].lower() == 'p '):
        new = ''
        while (new not in ['Q', 'R', 'B', 'KN']):
            new = input("Choose what the pawn should promoted to? (Q/R/B/KN): ").upper()
        if game.turn == 'Green':
            game.board[game.fy][game.fx] = new.upper() + ' '
        else:
            game.board[game.fy][game.fx] = new.lower() + ' '

def rotateBoard(board):
    tempBoard = newBoard()
    for x in range (10):
        for y in range (10):
            tempBoard[x][y] = board[9-x][9-y]
    return tempBoard
