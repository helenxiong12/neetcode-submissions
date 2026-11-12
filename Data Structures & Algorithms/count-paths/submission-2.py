class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(1, m):
            # new_row = row
            prev = 1
            for j in range(1, n):
                # if j == 0:
                #     new_row[j] = 1
                # else:
                #     new_row[j] = new_row[j-1] + row[j]
                tmp = row[j]
                row[j] = prev + row[j]
                prev = row[j] # tmp
            # row = new_row
        return row[-1]