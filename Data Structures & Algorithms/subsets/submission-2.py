class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allsets = []
        def helper(nums, idx, subset):
            if idx == len(nums):
                allsets.append(subset[:])
                return
            subset.append(nums[idx])
            helper(nums, idx + 1, subset)
            subset.pop()
            helper(nums, idx + 1, subset)
        helper(nums, 0, [])
        return allsets