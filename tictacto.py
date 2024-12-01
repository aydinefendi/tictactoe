# By Al Yaman Al-Naabi
# The strcuture of the board
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
# Setting the initial player to "X"
currentplayer = "X"
# Variable to store the winner initially None
winner = None
# Flag to keep the game running, initially set to True
gamerunning = True

print("Welcome to Tic-Tac-Toe game By Al Yaman Al-Naabi, Abdullah Al Lawaati and Aydin Efendi!")

# By Aydin Efendi
# Function to display the current state of the game board
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2]) # First row
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5]) # Second row
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8]) # Third row

# By Aydin Efendi
def playerinput(board):
    global gamerunning # Accessing the global variable to allow quitting the game
    while True:  # Infinite loop to ensure valid input
        try:
            print("Press 0 if you want to quit the game.") # Message for a player to be able to quit
            inp = int(input("Choose a number from 1 to 9: ")) # Taking an input from a player form 1 to 9
            if inp == 0:  # If player inputs 0 we will stop the game
                gamerunning = False # Enables us to stop the game
                print("You have quit the game.")
                break
            #Check if the input is within the range and the position is empty 
            if inp >= 1 and inp <= 9 and board[inp-1] not in ["X", "O"]:
                board[inp-1] = currentplayer # Mark the position with players symbol
                break
            else:
                print("Invalid input. Please choose an empty position.") # Print this if the inout is not valid
        except ValueError:
            print("Please enter a valid number between 1 and 9.") # Print this if the input is not integer

# By Aydin Efendi
def checkhorizontale(board): #Checking if there are 3 in a row horizontally 
    global winner
    for i in range(0, 9, 3): # Loop through each row
        if board[i] == board[i+1] == board[i+2] and board[i] != "-": # 
            winner = board[i] #Asign winner to the player's symbol
            return True
    return False # Return false if no winner found

def checkrow(board): #This function checks the vertical rows (columns)
    global winner
    for i in range(3): # Increment by 1 to check columns
        if board[i] == board[i+3] == board[i+6] and board[i] != "-": # Check if all cells in the column are the same
            winner = board[i] #Set the winner to the players symbol
            return True
    return False # Return false if no winner found 

# By Al Yaman Al-Naabi
def checkdiagnol(board): #Checking if there are 3 in a row diagonally
    global winner
    # Check the first diagonal (top-left to bottom-right)
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    # Check the second diagonal (top-right to bottom-left)
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[4]
        return True
    return False #Return false if the winner is not found

# By Al Yaman Al-Naabi
def checktie(board): # Function to check if its a tie or not 
    global gamerunning
    if all(position in ["X", "O"] for position in board):  # Check if all positions are filled
        printboard(board)
        print("It is a Tie!") # If True prints a tie
        gamerunning = False # And stops the game

# By Abdullah Al-Lawaati
def checkwin(): # Function to check for a winner
    if checkdiagnol(board) or checkhorizontale(board) or checkrow(board):
        print(f"The winner is {winner}") # Printing the winner 
        global gamerunning
        gamerunning = False # Stop thre game

# By Abdullah Al-Lawaati
def swichplayer(): # Function to switch the current player
    global currentplayer
    # Switch between O and X players
    currentplayer = "O" if currentplayer == "X" else "X"

# By Abdullah Al-Lawaati
while gamerunning: # Continue the game while gamerunning is True
    printboard(board) # Display the current board state
    playerinput(board) # Take input from the current player
    if not gamerunning:  # If the user quits break out of the loop
        break
    checkwin() #Checking if there is a winner
    if gamerunning: # If no winner, check for a tie
        checktie(board)
    if gamerunning: # If no tie, switch to the next player
        swichplayer()

#Game over message
print("Game over")