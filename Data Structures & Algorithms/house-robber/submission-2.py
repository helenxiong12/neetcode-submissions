class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        arr = [0 for _ in range(len(nums))]
        arr[0] = nums[0]
        for i in range(1, len(nums)):
            rob2 = nums[i] 
            if i >= 2:
                rob2 += arr[i-2]
            rob1 = arr[i-1]
            arr[i] = max(rob2, rob1)
        return arr[-1]

        