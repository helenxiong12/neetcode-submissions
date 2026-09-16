class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[-1] * len(s) for _ in range(len(s))]
        res = []
        def isPalindrome(start, end) -> bool:
            # print(start, end, dp[start][end-1])
            a, b = start, end - 1
            # if dp[start][end-1] != -1:
                # print("dp[" + str(start) + "][" + str(end-1) + "]", dp[start][end-1])
                # return dp[start][end-1]

            while a < b:
                if s[a] != s[b]:
                    # dp[start][end-1] = 0
                    return 0
                a += 1
                b -= 1
            # dp[start][end-1] = 1 # end - start + 1  # len of substring
            return 1 # dp[start][end-1]
    
        def recurse(start, path):
            # print("recurse", start, path)
            if start == len(s): # reached the end
                # print("end", path)
                res.append(path[:])
                return

            # iterate from start to end of string
            for i in range(start+1, len(s)+1): 
                # print("iter", start, i)
                if isPalindrome(start, i):
                    # print("pali", start, i)
                    path.append(s[start:i])
                    recurse(i, path)
                    path.pop()
        
        recurse(0, [])
        return res

                    