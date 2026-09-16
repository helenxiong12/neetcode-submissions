class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, partial):
            if idx == len(nums):
                res.append(partial.copy())
                return
            partial.append(nums[idx])
            dfs(idx+1, partial)
            partial.pop()
            dfs(idx+1, partial)
        
        dfs(0, [])
        return res
        