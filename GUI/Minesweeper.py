from random import randrange
from tkinter import messagebox
from tkinter import *
from time import time

window = None
firstClick = True
size = 0
numMines = 0
flagged = 0
defused = 0
btns = []
mines = []
board = []
move = ""

def format_time(elap):
    hours = int(elap / 3600)
    minutes = int(elap / 60 - hours * 60.0)
    seconds = int(elap - hours * 3600.0 - minutes * 60.0)
    hseconds = int((elap - hours * 3600.0 - minutes * 60.0 - seconds) * 10)
    return '%02d:%02d:%02d:%1d' % (hours, minutes, seconds, hseconds)

def plantMines():
    global numMines
    global mines
    count = 0
    mines = []
    if (numMines == 0):
        numMines = randrange(1,15)
    while (count < numMines):
        x = randrange(0,size)
        y = randrange(0,size)
        while ([x,y] in mines):
            x = randrange(0,size)
            y = randrange(0,size)
        mines.append([x, y])
        count += 1
    mines.sort()

def getNeighbourMines(x, y):
    count = 0
    if (x != 0 and                      [x-1, y] in mines):     count += 1
    if (x != size and                   [x+1, y] in mines):     count += 1
    if (y != 0 and                      [x, y-1] in mines):     count += 1
    if (y != size and                   [x, y+1] in mines):     count += 1
    if (x != 0 and y != 0 and           [x-1, y-1] in mines):   count += 1
    if (x != size and y != 0 and        [x+1, y-1] in mines):   count += 1
    if (x != 0 and y != size and        [x-1, y+1] in mines):   count += 1
    if (x != size and y != size and     [x+1, y+1] in mines):   count += 1
    return count

def updateBoard(x, y):
    global firstClick
    global startTime
    if (firstClick == True):
        while ([x, y] in mines):
            plantMines()
        firstClick = False
        startTime = time()
    if ([x, y] in mines):
        btns[x][y].config(text = '*', bg = "RED", fg = "WHITE", font = (15))
        gameOver(False)
    else:
        count = getNeighbourMines(x, y)
        if (count != 0):    btns[x][y].config(text = count, bg = "GREEN")
        else:               btns[x][y].config(text = ' ', bg = "GREEN");    expandBoard(x, y)

def expandBoard(x, y):
    if (x != 0 and btns[x-1][y]["text"] == '' and                           [x-1, y] not in mines):     updateBoard(x-1, y)
    if (x != size-1 and btns[x+1][y]["text"] == '' and                      [x+1, y] not in mines):     updateBoard(x+1, y)
    if (y != 0 and btns[x][y-1]["text"] == '' and                           [x, y-1] not in mines):     updateBoard(x, y-1)
    if (y != size-1 and btns[x][y+1]["text"] == '' and                      [x, y+1] not in mines):     updateBoard(x, y+1)
    if (x != 0 and y != 0 and btns[x-1][y-1]["text"] == '' and              [x-1, y-1] not in mines):   updateBoard(x-1, y-1)
    if (x != size-1 and y != 0 and btns[x+1][y-1]["text"] == '' and         [x+1, y-1] not in mines):   updateBoard(x+1, y-1)
    if (x != 0 and y != size-1 and btns[x-1][y+1]["text"] == '' and         [x-1, y+1] not in mines):   updateBoard(x-1, y+1)
    if (x != size-1 and y != size-1 and btns[x+1][y+1]["text"] == '' and    [x+1, y+1] not in mines):   updateBoard(x+1, y+1)

def leftClick(x, y):
    # print(x, y)
    updateBoard(x, y)

def rightClick(event, x, y):
    global flagged
    global defused
    btn = event.widget
    if (btn["text"] == ''):
        btn.config(text = '!', bg = "WHITE")
        if ([x, y] in mines):     defused += 1
        flagged += 1
    elif (btn["text"] == '!'):
        btn.config(text = '', bg = "Grey")
        if ([x, y] in mines):     defused -= 1
        flagged -= 1

def buttonClicked(event, x=None, y=None):
    global defused
    global numMines
    global timePassed
    if (event.num == 1 and btns[x][y]["text"] == ''):   leftClick(x, y)
    elif (event.num == 3):                              rightClick(event, x, y)
    if (defused == numMines):                           gameOver(True)
    # print("Defused:", defused, "Flagged:", flagged)
    timePassed.set(format_time(time() - startTime))

def newBoard():
    global btns
    global window
    global lab

    window = Tk()
    window.title("Minesweeper")
    # window.geometry("600x600")
    window.resizable (0,0)
    
    # Randomize mine positions
    plantMines()
    # print(mines)

    # Frame for info
    info = Frame(window)
    info.grid(row = 0)
    global timePassed
    timePassed = StringVar()
    lab = Label(info, textvariable = timePassed)
    lab.grid(row=0, sticky="wens")
    # lab.pack()
    
    # Frame for game buttons
    grid = Frame(window)
    # grid.rowconfigure(0, weight = 1)
    grid.grid(row = 1)
    
    btns = []
    for x in range(size):
        btns.append([])
        for y in range(size):
            # grid.columnconfigure(y, weight = 1)
            
            xy = Frame(grid)
            # xy.columnconfigure(0, weight = 1)
            # xy.rowconfigure(0, weight = 1)
            xy.grid(column = y, row = x)
            
            xyb = Button(xy, text = '', height = 30//size, width = 60//size, bg = "Grey", font = (15))
            xyb.grid(column = y, row = x, sticky = "wens")
            xyb.bind("<Button>", lambda event, row = x, column = y : buttonClicked(event, row, column))
            # xyb.pack()
            btns[x].append(xyb)
    
    # Frame for menu buttons
    butFrame = Frame(window)
    butFrame.grid(row = 2)
    
    newGameBtn = Button(butFrame, text = "New Game", height = 2, width = 30, bg = "GREEN", fg = "WHITE", command = newGame)
    newGameBtn.grid(column = 0, row = 0, sticky = "wens")
    # newGameBtn.pack()
    quitBtn = Button(butFrame, text = "Quit Game", height = 2, width = 30, bg = "RED", fg = "WHITE", command = quitGame)
    quitBtn.grid(column = 1, row = 0, sticky = "wens")
    # quitBtn.pack()

def close():
    window.destroy()

def newGame():
    global firstClick
    global flagged
    global defused
    firstClick = True
    flagged = 0
    defused = 0
    window.destroy()
    newBoard()

def quitGame():
    print("################# Game Over! #################\n")
    quit()

def revealMines():
    global mines
    for mine in mines:
        if (btns[mine[0]][mine[1]]["text"] != '!'):
            btns[mine[0]][mine[1]].config(text = '*', bg = "RED", fg = "WHITE", font = (15))

def gameOver(win):
    global lab
    revealMines()
    if (not win):
        lab["text"] = "You Lost :("
        reply = messagebox.askquestion("You Lost :(", "You hit a mine! Would you like to try again?", icon="error")
    elif (win):
        lab["text"] = "You Won! :)"
        reply = messagebox.askquestion("You Won! :)", "You Won! Do you want to play another game?", icon="error")
    if reply == "yes":  newGame()
    else:               quitGame()

# The main
print("[Enter q to exit game]")
while (not 5 <= size <= 15):
    size = input("Enter the size of the board (5 - 15): ").strip()
    if (size.isdigit()):    size = int(size)
    else:                   size = 0
custom_mines = input("Enter the number of mines (Optional): ").strip()
if (custom_mines.isdigit() and int(custom_mines) <= (size**2) - 1):
    numMines = int(custom_mines)
newBoard()
startTime = None

window.mainloop()
