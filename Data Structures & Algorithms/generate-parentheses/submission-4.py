class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # idea: backtrack with pruning
        # keep open count and closed count
        # if open count >= n: prune, or add closed
        # on each path: append closing parenthesis, or continue to 
        res = []
        s = []
        def recurse(o, c):
            if o == c == n:
                res.append("".join(s))
                return

            if o < n:
                s.append("(")
                recurse(o + 1, c)
                s.pop()
            
            if c < o:
                s.append(")")
                recurse(o, c + 1)
                s.pop()
        recurse(0, 0)
        return res