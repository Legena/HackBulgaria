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
    move = int(input("Enter move (0..8)>"))
    while(True):
        if board[move] == 0:
            board[move] = -1
            break
        else:
            print("Invalid move!")
        move = int(input("Enter move (0..8)>"))



def get_value(number):
    if number == -1:
        return 'X'
    elif number == 0:
        return '-'
    else:
        return 'O'


def print_board(board):
    for i in range(0, 3):
        a = get_value(board[i*3])
        b = get_value(board[i*3 + 1])
        c = get_value(board[i*3 + 2])
        print("{}|{}|{}".format(a, b, c))

def main():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("You - X. AI - O.")
    for turn in range(0, 9):
        if(is_winner(board) == 0):
            if turn % 2 == 0:
                print_board(board)
                player_move(board)
            else:
                computer_move(board)
    print(is_winner(board))


if __name__ == '__main__':
    main()