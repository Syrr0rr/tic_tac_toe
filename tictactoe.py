row1 = ["-", "-", "-",]
row2 = ["-", "-", "-",]
row3 = ["-", "-", "-",]
Board = [row1, row2, row3]
def print_board(): 
    '''Prints the board'''
    for i in range(len(Board)):
        print(Board[i])
        print()
 
def get_validint(prompt="Enter positive int") :
    '''Asks user for input intil valid'''
    user_input = input(prompt)  
    while user_input.isdigit() == False:
        print("Invalid.")
        user_input = input(prompt)  
    return int(user_input)
 
 
def player_go(symbol): #maybe combine both player functions into 1?
    '''Starts player turn'''
    X_row = get_validint(f"{symbol} row (1-3): ")
    X_column = get_validint(f"{symbol} column(1-3): ")
    X_row = X_row - 1
    X_column = X_column - 1
    if (X_row > 2 or X_column > 2) or (X_row < 0 or X_column < 0):
        print("You went over ")
        X_row = get_validint(f"{symbol} row: ")
        X_column = get_validint(f"{symbol} column: ")

    while Board[X_row] [X_column] != "-": #can make != "-"
        print("Something is already there")
        X_row = get_validint(f"{symbol} row: ")      #somehow adds 1 to row and column
        X_column = get_validint(f"{symbol} column: ")
        X_row = X_row - 1
        X_column = X_column - 1
    Board[X_row] [X_column] = symbol
 
def check_diagonal():
    '''Checks diagonal from bottem left to top right'''
    if Board[2][0] == Board[1][1] == Board[0][2] and Board[0][2] != "-":
        return Board[2][0]
 
    else:
        return "No winner"
   
def find_result(player = "X"):
    '''Finds if anyone has won'''
    for row in range(len(Board)):
        if Board[row] == [player, player, player]: #check for win left - right
            return player
        for column in range(3):
            if Board[0][column] == player and Board[1][column] == player and Board[2][column] == player: #checks win going up-down
                return player
        lup_dright = 0
        for i in range(3):
            if Board[i][i] == player:                                           
                lup_dright =+ 1         
                if lup_dright == 3:
                    return player
        dleft_uright = check_diagonal()
        if dleft_uright == "X":
            return "X"
        elif dleft_uright == "O":
            return "O"
    return f"player {player} didnt"


def reset():
    '''resets the board'''
    global another_round
    if result == "X" or result == "O" or num_dash == 0: #if the result isnt one of these then it is skipped
        replay = input("replay? (y/n)")
        if replay == "y":
            for row in range(len(Board)):
                for col in range(len(Board)):
                        Board[row][col] = "-"
            another_round = True    
        else:
            another_round = False


def count_dash():
    count = 0
    for row in range(len(Board)):
        for col in range(len(Board)):
            if Board[row][col] == "-":
                count += 1
    return count
active_player = "X"
another_round = True


while another_round:
    global num_dash
    num_dash = count_dash()
    print_board()
    print(num_dash)
    if num_dash == 0:
        print("Tie")
        reset()
    player_go(active_player)
    result = find_result(active_player)
    print(f"{result} win")
    reset()
    active_player = "O" if active_player == "X" else "X" #plays even if the player before put a thing over a space already taken