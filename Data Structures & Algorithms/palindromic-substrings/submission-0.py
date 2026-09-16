class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for center in range(len(s)):
            # odd palindromes
            i, j = center, center
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            # even palindromes
            i, j = center, center + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
        return res

        