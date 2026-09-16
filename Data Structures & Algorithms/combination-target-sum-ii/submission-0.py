class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, partial, total):
            if total == target:
                res.append(partial.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            
            partial.append(candidates[idx])
            dfs(idx+1, partial, total + candidates[idx])
            partial.pop()

            while idx < len(candidates)-1 and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1, partial, total)
        dfs(0, [], 0)
        return res