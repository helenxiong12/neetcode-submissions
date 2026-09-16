class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.res = []
        
        def isValid(self, row, col, n):
            print("checking", row, col)
            for c in range(n):
                if c != col and self.board[row][c] == 'Q':
                    return False
            for r in range(n):
                if r != row and self.board[r][col] == 'Q':
                    print("ret", 1)
                    return False

            r, c = row, col
            while r > 0 and c > 0:
                r -= 1
                c -= 1
            while r < n and c < n:
                if r != row or c != col:
                    if self.board[r][c] == 'Q':
                        print("ret", 2)
                        return False
                r += 1
                c += 1
            
            r, c = row, col
            while r > 0 and c < n - 1:
                r -= 1
                c += 1
            while r < n and c > -1:
                if r != row or c != col:
                    print(r, c)
                    if self.board[r][c] == 'Q':
                        print("ret", r, c, 3)
                        return False
                r += 1
                c -= 1
            return True

        def recurse(self, col, n):
            if col == n:
                print("hello")
                print(self.board)
                self.res.append(["".join(r) for r in self.board])
                return True

            for r in range(n):
                if isValid(self, r, col, n):
                    self.board[r][col] = 'Q'
                    recurse(self, col+1, n)
                    self.board[r][col] = '.'

        recurse(self, 0, n)
        return self.res
        
            
        