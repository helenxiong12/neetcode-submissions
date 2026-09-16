class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def recurse(o, c, s):
            # print(o, c, s)
            if o == c == n:
                res.append("".join(s))
                return
            if c > o or o > n:
                return
            if o < n:
                s.append("(")
                recurse(o + 1, c, s)
                s.pop()
            s.append(")")
            recurse(o, c+1, s)
            s.pop()

        recurse(0, 0, s)
        return res

            
            
        