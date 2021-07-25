from Board import *
from Moves import *
from os import system, name
from tkinter import *

class Game():
    def __init__(self, size):
        self.root = Tk()
        self.gameOver = False
        self.firstClick = True
        self.size = size
        self.gameBoard = GameBoard(self.root)
        self.btns = []
        # self.board = self.gameBoard.newBoard(self.root, size)
        self.board = newBoard(size)
        # self.board = GameBoard(self.root, size)
        self.numMines = 0
        self.mines = []
        self.move = ""
        self.x = -1
        self.y = -1

def main():
    print("[Enter q to exit game]")
    size = 0
    while (not 5 <= size <= 15):
        size = input("Enter the size of the board (5 - 15): ").strip()
        if (size.isdigit()):    size = int(size)
        else:                   size = 0
    game = Game(size)
    game.board = game.gameBoard.newBoard(game.root, game)
    game.board = newBoard(size)
    custom_mines = input("Enter the number of mines (Optional): ").strip()
    if (custom_mines.isdigit() and int(custom_mines) <= (size**2) - 1):
        game.numMines = int(custom_mines)
    plantMines(game)
    print(game.mines)

    # for x in game.board:
    #     print(x)
    # print(game.numMines, game.mines)

    printBoard(game.size, game.board)
    
    while (not game.gameOver):
        game.move = input("Enter your next move (cell coordinate): ").strip()

        if (game.move == 'q'):
            game.gameOver = True
            continue

        if (isValidMove(game)):
            updateBoard(game, game.x, game.y)
            
             # try:
            #     col, row = get_terminal_size()
            # except OSError:
            #     col, row = popen('stty size', 'r').read().split()
            # print("\n"*(int(col)-28))
            # cls = lambda: system('cls' if name =='nt' else 'clear')
            # cls()
            # os.system('clear')

            printBoard(game.size, game.board)
    
    print("################# Game Over! #################\n")
    exit()

# class Minesweeper():
#     def __init__(self, parent):
#         self.parent = parent
#         self.hello_button = Button(parent, text = "Hello", command = self.say_hi)
#         self.hello_button.grid(column = 0, row = 0)
#         # When Quit button is pressed, special function parent.destroy is called which destroys the window
#         self.quit_button = Button(parent, text = "Quit", fg = "red", command = exit)
#         self.quit_button.grid(column = 1, row = 0)\
    
#     def say_hi(self):
#         print("Hi there!")
    
#     def exit(self):
#         self.parent.quit()

if __name__ == '__main__':
    main()