class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        chosen = [False] * len(nums)
        res = []

        def dfs(chosen, candidates):
            if not candidates: # we've used up everything 
                res.append(chosen.copy())
                return

            for i in range(len(candidates)):
                chosen.append(candidates[i])
                dfs(chosen, candidates[:i] + candidates[i+1:])
                chosen.pop()
        dfs([], nums)
        return res 
        
        