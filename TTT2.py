# Tic-Tac-Toe Game in Python

def print_board(board):
    print(f"""
     {board[0]} | {board[1]} | {board[2]}
    -----------
     {board[3]} | {board[4]} | {board[5]}
    -----------
     {board[6]} | {board[7]} | {board[8]}
    """)

def check_win(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    return " " not in board

def tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"
    
    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
        
        if board[move] != " ":
            print("Invalid move, try again!")
            continue
        
        board[move] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
