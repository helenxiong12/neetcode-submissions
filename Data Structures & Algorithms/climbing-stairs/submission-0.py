class Solution:
    def climbStairs(self, n: int) -> int:
        i, j = 0, 1
        for _ in range(n):
            tmp = i + j
            i = j
            j = tmp
        return j
        