class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # fwd array       [1, 1, 2, 8, 48]
        # bkd array [48, 48, 24, 6, 1]
        mult = 1
        fwd = [1]
        for i in range(len(nums) - 1):
            fwd.append(nums[i] * mult)
            mult *= nums[i]

        mult = 1
        bkd= [1] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            bkd[i-1] = bkd[i] * nums[i]
        
        # print(fwd)
        # print(bkd)

        return [fwd[i] * bkd[i] for i in range(len(nums))]