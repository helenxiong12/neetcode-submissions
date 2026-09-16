class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, partial, total):
            # print(idx, partial, total, target)
            if total == target:
                # print("res", partial)
                res.append(partial.copy())
                return
            if total > target or idx > len(nums) -  1:
                return
            
            # print(idx, partial, total, target)
            partial.append(nums[idx])
            dfs(idx, partial, total+nums[idx])
            partial.pop()
            dfs(idx+1, partial, total)
        
        dfs(0, [], 0)
        return res
        