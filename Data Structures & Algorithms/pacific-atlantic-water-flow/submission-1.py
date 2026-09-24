class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = [[0] * cols for _ in range(rows)]
        atlantic = [[0] * cols for _ in range(rows)]
        visitedPacific = [[0] * cols for _ in range(rows)]
        visitedAtlantic = [[0] * cols for _ in range(rows)]

        reachable = []
        for r in range(rows):
            for c in range(cols):
                if r == 0:
                    pacific[r][c] = 1
                    visitedPacific[r][c] = 2
                if r == rows - 1:
                    atlantic[r][c] = 1
                    visitedAtlantic[r][c] = 2
                if c == 0:
                    pacific[r][c] = 1
                    visitedPacific[r][c] = 2
                if c == cols - 1:
                    atlantic[r][c] = 1
                    visitedAtlantic[r][c] = 2

        def inBounds(r, c):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1:
                return False
            return True

        def dfsPacific(r, c):
            if visitedPacific[r][c] == 2: # complete
                return pacific[r][c]
            if visitedPacific[r][c] == 1:
                return False

            visitedPacific[r][c] = 1 # mark as in progress 
            if inBounds(r-1, c) and heights[r-1][c] <= heights[r][c] and dfsPacific(r-1, c):
                visitedPacific[r][c] = 2
                pacific[r][c] = 1
                return True
            
            if inBounds(r+1, c) and heights[r+1][c] <= heights[r][c] and dfsPacific(r+1, c):
                visitedPacific[r][c] = 2
                pacific[r][c] = 1
                return True

            if inBounds(r, c-1) and heights[r][c-1] <= heights[r][c] and dfsPacific(r, c-1):
                visitedPacific[r][c] = 2
                pacific[r][c] = 1
                return True

            if inBounds(r, c+1) and heights[r][c+1] <= heights[r][c] and dfsPacific(r, c+1):
                visitedPacific[r][c] = 2
                pacific[r][c] = 1
                return True
            visitedPacific[r][c] = 2
            # pacific[r][c] = 0
            return False
    
        def dfsAtlantic(r, c):
            if visitedAtlantic[r][c] == 2:
                return atlantic[r][c]
            if visitedAtlantic[r][c] == 1:
                return False
            visitedAtlantic[r][c] = 1 # mark as visited
            if inBounds(r-1, c) and heights[r-1][c] <= heights[r][c] and dfsAtlantic(r-1, c):
                visitedAtlantic[r][c] = 2
                atlantic[r][c] = 1
                return True
            
            if inBounds(r+1, c) and heights[r+1][c] <= heights[r][c] and dfsAtlantic(r+1, c):
                visitedAtlantic[r][c] = 2
                atlantic[r][c] = 1
                return True

            if inBounds(r, c-1) and heights[r][c-1] <= heights[r][c] and dfsAtlantic(r, c-1):
                visitedAtlantic[r][c] = 2
                atlantic[r][c] = 1
                return True

            if inBounds(r, c+1) and heights[r][c+1] <= heights[r][c] and dfsAtlantic(r, c+1):
                visitedAtlantic[r][c] = 2
                atlantic[r][c] = 1
                return True
            visitedAtlantic[r][c] = 2
            # atlantic[r][c] = 0
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfsPacific(r, c) and dfsAtlantic(r, c):
                    reachable.append((r, c))
        print(pacific)
        print(atlantic)
        return reachable


            
