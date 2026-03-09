def docFile(fpath="MADITUAN.INP"):
    with open(fpath, "rt") as f:
        line = f.readline().split()
        N = int(line[0])
        x0 = int(line[1])
        y0 = int(line[2])
    return N, x0, y0
def KnightTour(N, x0, y0):
    board = [[0]*N for _ in range(N)]
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]
    board[x0][y0] = 1
    def hopLe(x,y):
        return 0 <= x < N and 0 <= y < N and board[x][y] == 0
    def quayLai(x,y):
        for i in range(8):
            if x + dx[i] == x0 and y + dy[i] == y0:
                return True
        return False
    def Try(step,x,y):
        if step == N*N:
            return True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if hopLe(nx,ny):

                board[nx][ny] = step + 1

                if Try(step+1,nx,ny):
                    return True

                board[nx][ny] = 0

        return False
    if Try(1,x0,y0):

        print(1)

        for row in board:
            print(*row)
    else:
        print(0)
def main():

    N, x0, y0 = docFile()

    KnightTour(N,x0,y0)

if __name__ == "__main__":
    main()