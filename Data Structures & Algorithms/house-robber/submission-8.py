class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        rob1 = 0
        rob2 = 0
        for i in range(len(nums)):
            tmp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2

        