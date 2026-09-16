class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[-1] * len(s) for _ in range(len(s))]
        res = []
        def isPalindrome(a, b) -> bool:
            # print(a, b, dp[a][b-1])
            start, end = a, b
            while start < end:
                if dp[a][b-1] != -1:
                    # print("dp[" + str(a) + "][" + str(b-1) + "]", dp[a][b-1])
                    return dp[a][b-1]
                if s[start] != s[end-1]:
                    dp[a][b-1] = 0
                    # print("dp[" + str(a) + "][" + str(b-1) + "]", dp[a][b-1])
                    return 0
                start += 1
                end -= 1
            dp[a][b-1] = b - a  # len of substring
            # print("dp[" + str(a) + "][" + str(b-1) + "]", dp[a][b-1])
            return dp[a][b-1]
    
        def recurse(start, path):
            # print("recurse", start, path)
            if start == len(s): # reached the end
                # print("end", path)
                res.append(path[:])
                return

            # iterate from start to end of string
            for i in range(start+1, len(s)+1): 
                # print("iter", start, i)
                if isPalindrome(start, i) > 0:
                    # print("pali", start, i)
                    path.append(s[start:i])
                    recurse(i, path)
                    path.pop()
        
        recurse(0, [])
        return res

                    