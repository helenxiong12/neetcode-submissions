class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        all_nums = set(nums)
        max_ct = 1
        for a in all_nums:
            if a-1 in all_nums:
                continue
            tmp = a
            while tmp+1 in all_nums:
                tmp+=1
            max_ct = max(tmp - a + 1, max_ct)
        return max_ct
        