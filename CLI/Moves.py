def isEmpty(game):
    pass

def isMine(cell, mines):
    pass

def getNeighbourMines(game, x, y):
    count = 0
    if (x != 0 and                              [x-1, y] in game.mines):    count += 1
    if (x != game.size and                      [x+1, y] in game.mines):    count += 1
    if (y != 0 and                              [x, y-1] in game.mines):    count += 1
    if (y != game.size and                      [x, y+1] in game.mines):    count += 1
    if (x != 0 and y != 0 and                   [x-1, y-1] in game.mines):  count += 1
    if (x != game.size and y != 0 and           [x+1, y-1] in game.mines):  count += 1
    if (x != 0 and y != game.size and           [x-1, y+1] in game.mines):  count += 1
    if (x != game.size and y != game.size and   [x+1, y+1] in game.mines):  count += 1
    return count

def isValidMove(game):
    move = game.move
    if (len(move) == 2 and move[0].isalpha() and move[1].isdigit()):
        game.x = ord(move[0]) - 97
        game.y = int(move[1]) - 1
        if (0 <= game.x < game.size and 0 <= game.y < game.size):
            print(game.x, game.y)
            return True
    print("Invalid move :(")
    return False