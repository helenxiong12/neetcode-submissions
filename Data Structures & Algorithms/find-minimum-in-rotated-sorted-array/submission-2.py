class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        i, j = 0, len(nums) - 2
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            else:
                if nums[mid] > nums[-1]:
                    i = mid + 1
                else:
                    j = mid 
        return -1
        