class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[-1] * len(s) for _ in range(len(s))]
        res = []
        def isPalindrome(start, end) -> bool:
            a, b = start, end - 1

            while a < b:
                if s[a] != s[b]:
                    return 0
                a += 1
                b -= 1
            return 1
    
        def recurse(start, path):
            if start == len(s): # reached the end
                res.append(path[:])
                return

            # iterate from start to end of string
            for i in range(start+1, len(s)+1): 
                if isPalindrome(start, i):
                    path.append(s[start:i])
                    recurse(i, path)
                    path.pop()
        
        recurse(0, [])
        return res

                    