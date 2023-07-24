class Solution:
    def get_neighbours(self, board, x, y):
        cand = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        result = []

        for c in cand:
            if c[0] > -1 and c[0] < len(board[0]) and c[1] > -1 and c[1] < len(board):
                result.append(c)

        return result

        
    def __exist(self, board, word, x, y, idx, used):
        if idx == len(word) - 1:
            return board[y][x] == word[idx]
        else:
            if board[y][x] == word[idx]:
                _n = self.get_neighbours(board, x, y)
                for point in _n:
                    if point not in used:
                        _used = used[:]
                        _used.append(point)
                        r = self.__exist(board, word, point[0], point[1], idx+1, _used)
                        if r:
                            return True
            else:
                return False
