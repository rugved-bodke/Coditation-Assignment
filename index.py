from typing import List

def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            lives = getLives(board, m, n, i, j)
            if board[i][j] == 0:
                if lives == 3:
                    board[i][j] = -1
            if board[i][j] == 1:
                if lives < 2 or lives > 3:
                    board[i][j] = 2

    for i in range(m):
        for j in range(n):
            if board[i][j] == -1:
                board[i][j] = 1
            if board[i][j] == 2:
                board[i][j] = 0
    print(board)
def getLives(board, m, n, i, j): 
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0),
                    (1, 1), (-1, -1), (-1, 1), (1, -1)]
    lives = 0
    for direction in directions:
        di = i + direction[0]
        dj = j + direction[1]
        if di >= 0 and di < m and dj >= 0 and dj < n:
            if board[di][dj] == 1 or board[di][dj] == 2:
                lives += 1
    return lives

board = []
for i in range(5):
    board.append(list(map(int, input().split(" "))))
print(board)
gameOfLife(board=board)