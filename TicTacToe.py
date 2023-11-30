def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]


def minimax(board, depth, maximizing_player):
    scores = {'X': 1, 'O': -1, 'tie': 0}

    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for row, col in get_empty_cells(board):
            board[row][col] = 'O'
            eval_score = minimax(board, depth - 1, False)
            board[row][col] = ' '
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in get_empty_cells(board):
            board[row][col] = 'X'
            eval_score = minimax(board, depth - 1, True)
            board[row][col] = ' '
            min_eval = min(min_eval, eval_score)
        return min_eval


def get_best_move(board):
    best_val = float('-inf')
    best_move = None

    for row, col in get_empty_cells(board):
        board[row][col] = 'O'
        move_val = minimax(board, 0, False)
        board[row][col] = ' '

        if move_val > best_val:
            best_move = (row, col)
            best_val = move_val

    return best_move


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("You win! Congratulations!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        print("Computer's turn:")
        computer_row, computer_col = get_best_move(board)
        board[computer_row][computer_col] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("Computer wins! Better luck next time.")
            break

        if is_board_full(board):
            print("It's a tie!")
            break


if __name__ == "__main__":
    main()
