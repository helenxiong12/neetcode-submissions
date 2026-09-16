class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inBounds(row, col):
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                return True
            return False

        def expandIsland(row, col):
            if grid[row][col] == "0" or grid[row][col] == "x":
                return # ocean or explored

            # left, right, up, down
            grid[row][col] = "x"
            if inBounds(row - 1, col):
                expandIsland(row-1, col)
            if inBounds(row + 1, col):
                expandIsland(row+1, col)
            if inBounds(row, col-1):
                expandIsland(row, col-1)
            if inBounds(row, col+1):
                expandIsland(row, col+1)
        islandCt = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "0" and grid[r][c] != "x":
                    expandIsland(r, c)
                    islandCt += 1
        return islandCt
