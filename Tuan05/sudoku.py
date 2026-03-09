def docTapTin(fpath="SUDOKU.INP"):

    board = []

    with open(fpath,"rt") as f:

        for line in f:
            board.append(list(line.strip()))

    return board


def hopLe(board,r,c,num):

    num = str(num)

    # kiểm tra dòng
    for j in range(9):
        if board[r][j] == num:
            return False

    # kiểm tra cột
    for i in range(9):
        if board[i][c] == num:
            return False

    # kiểm tra ô 3x3
    sr = (r//3)*3
    sc = (c//3)*3

    for i in range(sr,sr+3):
        for j in range(sc,sc+3):
            if board[i][j] == num:
                return False

    return True


def Try(board):

    for i in range(9):
        for j in range(9):

            if board[i][j] == '.':

                for num in range(1,10):

                    if hopLe(board,i,j,num):

                        board[i][j] = str(num)

                        if Try(board):
                            return True

                        board[i][j] = '.'

                return False

    return True


def main():

    board = docTapTin()

    if Try(board):

        for row in board:
            print("".join(row))

    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()