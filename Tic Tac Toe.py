import random


# Function to write results in log file
def write_to_file(name1,name2,result):
    file = open("log.txt","a")
    result_string = ""
    if(result == 0):
        result_string = f'{name1} won'
    elif(result == 1):
        result_string = f'{name2} won'
    else:
        result_string = 'draw'
    
    file_string = f'Players {name1}, {name2}, Result: {result_string}\n'
    file.write(file_string)
    file.close()

# Function to return player name based on symbol
def player_symbol(symbol, x_player, o_player):
    if symbol.lower() == "x":
        return x_player
    else:
        return o_player
    
    
# Function to print board 
def print_board(board):
    for i in range(3):
        row = ""
        for j in range(3):
            row += board[i][j] + "  |  "
        print(row)

# Function to check if board cell is not taken
def valid_input(board, i , j):
    if board[i][j] == "-":
        return True
    else:
        return False

# Function to toggle symbol
def change_symbol(symbol):
    if symbol.lower() == "x":
        return "O"
    else:
        return "X"
    
def check_winner(board):
    
    winner = False
    symbol = ""
    # Check rows
    for i in range(3):
        if(board[i][0] != "-" and board[i][0] == board[i][1] == board[i][2]):
            winner = True
            symbol = board[i][0]
            return winner, symbol
    # Check columns
    for j in range(3):
        if(board[0][j] != "-" and board[0][j] == board[1][j] == board[2][j]):
            winner = True
            symbol = board[0][j]
            return winner, symbol
    
    # Check cross
    if(board[0][0] != "-" and board[0][0] == board[1][1] == board[2][2]):
        winner = True
        symbol = board[0][0]
        return winner, symbol
    
    if(board[0][2] != "-" and board[0][2] == board[1][1] == board[2][0]):
        winner = True
        symbol = board[0][2]
        return winner, symbol
    
    return winner, symbol


# Check if board is full
def board_full(board):
    for row in board:
        if ("-") in row:
            return False
    return True



def start_game():
    x_player = input("Enter your name: ")
    o_player = input("Enter your name: ")
    symbol = random.choice(["X", "O"])
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    print_board(board)
    while True:
        player = player_symbol(symbol, x_player, o_player)
        print(f'Player: {player}, Sympol: {symbol}')
        
        while True:
            i,j = [int(x) for x in input("Enter the place: ").split()]
            if valid_input(board,i,j) == True:
                break
            print("Invalid input, Try again")
        board[i][j] = symbol
        print_board(board)
        # Check if anyone has won
        winner, winner_symbol = check_winner(board)
        if winner:
            winner_player = player_symbol(winner_symbol, x_player, o_player)
            print(f"{winner_player} won!")
            if(winner_symbol.lower() == "x"):
                result = 0
            else:
                result = 1
            
            write_to_file(x_player, o_player, result)
            print()
            show_menu()
            break
        # Check if board is full
        is_full = board_full(board)
        if is_full:
            print("Draw")
            result = 2
            write_to_file(x_player, o_player, result)
            print()
            show_menu()
            break
        symbol = change_symbol(symbol)

# Read from file to show results
def show_result():
    file = open("log.txt","r")
    print(file.read())
    file.close()
    print()
    show_menu()
    
def show_menu():
    print("Welcome")
    print("1) Start a new game")
    print("2) Show results")
    print("3) Exit")
    option = int(input())
    if (option == 1):
        start_game()
    elif (option == 2):
        show_result()
    else:
        exit()

show_menu()