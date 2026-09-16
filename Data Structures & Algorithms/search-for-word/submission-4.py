class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        # visited = [[False] * cols for _ in range(rows)]

        def recurse(idx, r, c):
            if board[r][c] != word[idx]:
                return False
            if idx == len(word)-1:
                return True
            tmp = board[r][c]
            board[r][c] = '#'
            if r-1 >= 0 and board[r-1][c] != '#' and recurse(idx+1, r-1, c):
                return True
            if r+1 < rows and board[r+1][c] != '#' and recurse(idx+1, r+1, c):
                return True
            if c-1 >= 0 and board[r][c-1] != '#' and recurse(idx+1, r, c-1):
                return True
            if c+1 < cols and board[r][c+1] != '#'  and recurse(idx+1, r, c+1):
                return True
            board[r][c] = tmp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if recurse(0, i, j):
                    return True
        return False
        
