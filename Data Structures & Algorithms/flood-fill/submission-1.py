class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # dfs
        row = len(image)
        col = len(image[0])
        visited = [[False for c in range(col)] for r in range(row)]

        def inBounds(r, c) -> bool:
            if r >= 0 and r < row and c >= 0 and c < col:
                return True
            return False
    
        def helper(r, c, oc):
            if visited[r][c] == True:
                return
            if image[r][c] != oc:
                return
            
            image[r][c] = color
            visited[r][c] = True
            if inBounds(r-1, c):
                helper(r-1, c, oc)
            if inBounds(r+1, c):
                helper(r+1, c, oc)
            if inBounds(r, c-1):
                helper(r, c-1, oc)
            if inBounds(r, c+1):
                helper(r, c+1, oc)


        helper(sr, sc, image[sr][sc])

        return image
