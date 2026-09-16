class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # fwd array       [1, 1, 2, 8, 48]
        # bkd array [48, 48, 24, 6, 1]
        n = len(nums)
        fwd = [1] * n
        for i in range(n - 1):
            fwd[i+1] = fwd[i] * nums[i]
\
        bkd= [1] * n
        for i in range(n - 1, 0, -1):
            bkd[i-1] = bkd[i] * nums[i]


        return [fwd[i] * bkd[i] for i in range(n)]