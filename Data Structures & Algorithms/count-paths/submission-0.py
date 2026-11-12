class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n)]
        for i in range(1, m):
            new_row = row
            for j in range(n):
                if j == 0:
                    new_row[j] = 1
                else:
                    new_row[j] = new_row[j-1] + row[j]
            row = new_row
        return row[-1]