def is_winner(board):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for win in wins:
        if(board[win[0]] != 0 and
        board[win[0]] == board[win[1]] and
        board[win[0]] == board[win[2]]):
            return board[win[2]]
    return 0


def minimax(board, player):
    winner = is_winner(board)
    if winner != 0:
        return winner*player

    move = -1
    score = -2
    for i in range(0, 9):
        if(board[i] == 0):
            board[i] = player
            this_score = -minimax(board, (player * -1))
            if this_score > score:
                score = this_score
                move = i
            board[i] = 0
    if move == -1:
        return 0
    return score


def computer_move(board):
    move = -1
    score = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            temp_score = -minimax(board, -1)
            board[i] = 0
            if temp_score > score:
                score = temp_score
                move = i
    board[move] = 1


def player_move(board):
    move = -1
    while(move >= 9 or move < 0 and board[move] == 0):
        move = int(input("Enter move (0..8)>"))
    board[move] = -1


def print_board(board):
    for x in range(0, 3):
        print("{}|{}|{}".format(board[3*x + 0], board[3*x + 1], board[3*x + 2]))


def main():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("You - X. AI - O.")
    for turn in range(0, 9):
        if(is_winner(board) == 0):
            if turn % 2 == 0:
                player_move(board)
            else:
                computer_move(board)
            print_board(board)
    print(is_winner(board))


if __name__ == '__main__':
    main()