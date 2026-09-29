class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_start, l_end = 0, 0
        def longestPalindromeHelper(s, l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1
        for i in range(len(s)):
            start, end = longestPalindromeHelper(s, i, i)
            start2, end2 = longestPalindromeHelper(s, i, i+1)
            if end - start > l_end - l_start:
                l_start, l_end = start, end
            if end2 - start2 > l_end - l_start:
                l_start, l_end = start2, end2
        return s[l_start:l_end + 1]

            
            
        