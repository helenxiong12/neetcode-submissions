class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        arr = [0 for _ in range(len(nums))]
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2

        