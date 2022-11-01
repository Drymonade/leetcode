class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def _queen(board, x, y):
            n = len(board)
            m = len(board[0])

            board[y] = board[y][:x] + 'Q' + board[y][x + 1:]

            for i in range(m):
                for j in range(n):
                    if (x == i or y == j or i - j == x - y or i + j == x + y) and not (x == i and y == j):
                        if board[j][i] != 'Q':
                            board[j] = board[j][:i] + 'X' + board[j][i + 1:]

        board = ['.'.join('' for _ in range(n + 1)) for _ in range(n)]

        def _solve(board, line, result):
            if line < n:
                if set(board[line]) != set('X'):
                    for i in range(n):
                        if board[line][i] != 'X':
                            _board = board[:]
                            _queen(_board, i, line)
                            _solve(_board, line + 1, result)
            else:
                result.append(board)

        _solve(board, 0, result)

        for board in result:
            for idx in range(n):
                board[idx] = board[idx].replace('X', '.')

        return result
