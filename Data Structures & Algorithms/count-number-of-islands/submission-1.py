class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def expandIsland(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return

            if grid[row][col] == "0" or grid[row][col] == "x":
                return # ocean or explored

            # left, right, up, down
            grid[row][col] = "x"
            expandIsland(row-1, col)
            expandIsland(row+1, col)
            expandIsland(row, col-1)
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
