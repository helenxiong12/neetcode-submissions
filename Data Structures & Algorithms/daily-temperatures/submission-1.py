class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        
        for i, j in zip(temperatures, range(n)):
            while len(stack) > 0 and stack[-1][0] < i:
                res[stack[-1][1]] = j - stack[-1][1]
                stack.pop()
            stack.append((i, j))

        return res

