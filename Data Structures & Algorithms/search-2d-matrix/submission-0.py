class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row
        l, r = 0, len(matrix) - 1
        width = len(matrix[0]) - 1
        row = -1
        if target < matrix[0][0] or target > matrix[len(matrix) - 1][width]:
            return False
        row = -1
        while l <= r:
            # print("loop a", l, r)
            mid = (l + r) // 2
            # if matrix[mid][0] == target or matrix[mid][width] == target:
            #    return True
            #else:
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][width]:
                l = mid + 1
            else:
                row = mid
                break
        # print("row", row)
        if row == -1:
            return False

        l, r = 0, width
        while l <= r:
            ("loop b", l, r)
            mid = (l + r) // 2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            elif target == matrix[row][mid]:
                return True
        
        return False
        
            
