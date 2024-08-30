import random

player = 'x'
opponent = 'o'

rows, cols = (3, 3)
board = [[0 for _ in range(cols)] for _ in range(rows)]

def print_board():
    for row in board:
        print(row)

def players_move():
     while True:
        try:
            number = int(input("Make your move by typing 1-9: "))
            if check_for_valid_move(number):
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_for_valid_move(number):
    #key value map
    mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }

    # Check if the move is within the valid range
    if number not in mapping:
        print("Invalid number. Please choose a number between 1 and 9.")
        return False

    row, col = mapping[number]

    # Check if the cell is empty
    if board[row][col] == 0:
        board[row][col] = player
        return True
    else:
        print("Cell is already occupied. Try again.")
        return False

def opponents_move():
    empty_cells = find_empty_cells()
    # Choose a random empty cell if available
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = opponent
      

def find_empty_cells():
    empty_cells = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                empty_cells.append((r, c))
    return empty_cells            

def chek_win(player):
    # Check horizontal rows for a win
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True
    # Check vertical columns for a win
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False        

def check_draw():
    empty_cells = find_empty_cells()

    if len(empty_cells) == 0:
        return True
    else:
        return False

def check_game_over():
    if chek_win(player):
        print(f"Player {player} wins!")
        return True
    elif chek_win(opponent):
        print(f"Opponent {opponent} wins!")
        return True
    elif check_draw():
        print("The game is a draw!")
        return True
    else:
        return False
    
def game_status():
    if check_game_over():
        print("Game over!")
    else:
        print("Game continues.")

print("Tic-Tac-Toe game in Python!")
# Main game loop
while True:
    print_board()
    players_move()
    if check_game_over():
        print_board()
        break
    print("Opponents move:")
    opponents_move()
    if check_game_over():
        print_board()
        break











