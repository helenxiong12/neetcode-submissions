class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        all_nums = set()
        for n in nums:
            if n in all_nums:
                return True
            all_nums.add(n)
        return False
        