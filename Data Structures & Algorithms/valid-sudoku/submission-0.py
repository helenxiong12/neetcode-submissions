class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows:
        squares = [set() for _ in range(9)]
        for i in range(9):
            seen_row = set()
            seen_col = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in seen_row:
                    # print("row", i, j)
                    return False
                else:
                    seen_row.add(board[i][j])
                if board[j][i] != '.' and board[j][i] in seen_col:
                    # print("col", i, j, board[j][i])
                    return False
                else:
                    seen_col.add(board[j][i])
                square_idx = (i // 3) * 3 + j // 3
                if board[i][j] != '.' and board[i][j] in squares[square_idx]:
                    # print("sq", i, j)
                    return False
                else:
                    squares[square_idx].add(board[i][j])
        return True

                
