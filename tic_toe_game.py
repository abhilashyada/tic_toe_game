def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == "O":
                return "Abhinav Wins"
            elif row[0] == "X":
                return "Anjali Wins"
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == "O":
                return "Abhinav Wins"
            elif board[0][col] == "X":
                return "Anjali Wins"
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "O":
            return "Abhinav Wins"
        elif board[0][0] == "X":
            return "Anjali Wins"
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "O":
            return "Abhinav Wins"
        elif board[0][2] == "X":
            return "Anjali Wins"
    return "Tie"

board = []
for _ in range(3):
    row = input().strip().split()
    board.append(row)
result = check_winner(board)
print(result)