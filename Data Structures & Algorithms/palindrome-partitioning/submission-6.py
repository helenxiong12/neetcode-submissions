class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = []

        for l in range(1,len(s)+1):
            for i in range(len(s)-l+1):
                # print(i, l)
                if s[i] == s[i+l-1] and (i+1 > i+l-2 or dp[i+1][i+l-2]):
                    dp[i][i+l-1] = True
                else:
                    dp[i][i+l-1] = False
                # print(dp)
    
        def recurse(start, path):
            if start == len(s): # reached the end
                res.append(path[:])
                return

            # iterate from start to end of string
            for i in range(start+1, len(s)+1): 
                # print(start, i)
                if dp[start][i-1]:
                    path.append(s[start:i])
                    recurse(i, path)
                    path.pop()
        
        recurse(0, [])
        return res

                    