class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # idea: backtrack with pruning
        # keep open count and closed count
        # if open count >= n: prune, or add closed
        # on each path: append closing parenthesis, or continue to 
        res = []
        def recurse(open, closed, s):
            if len(s) == 2*n:
                res.append(s)
                return

            if open < n:
                recurse(open + 1, closed, s + "(")
            
            if closed < n and closed < open:
                recurse(open, closed + 1, s + ")")
        recurse(0, 0, "")
        return res