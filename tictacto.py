board = ["-", "-", "-",
        "-", "-", "-",
         "-", "-", "-"]

currentplayer = "X"
winer = None
gamerunning = True

print("Welcome to Tic-Tac-Toe game !")
print("-----------")
# printing the game board 

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input 

def playerinput(board):
    inp = int(input("Choose number form 1 to 9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("You can not play in that position, place is occupied")

# check for winner or tie(horizontal, diagnol, row)

def checkhorizontale(board):
    global winer 
    if board[0] == board[1] == board[2] and board[1] != "-":
        winer = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winer = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winer = board[7]
        return True

def checkrow(board):
    global winer 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winer = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winer = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[8] != "-":
        winer = board[8]
        return True
    
def checkdiagnol(board):
    global winer 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winer = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winer = board[4]
        return True
    
def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("It is Tie !")
        gamerunning = False

def checkwin():
    if checkdiagnol(board) or checkhorizontale(board) or checkrow(board):
        print(f"The winner is {winer}")


# swich the player 
# there is no need to write board with in pracits, cus we just swicking players without channging the board

def swichplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

# check for win of tie again 

while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    swichplayer()