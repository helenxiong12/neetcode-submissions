class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = set(s[0])

        start, end = 0, 1
        maxlen = 1
        while start < end and end < len(s):
            if s[end] in seen:
                while s[start] in seen and s[start] != s[end] and start < end:
                    seen.remove(s[start])
                    start += 1
                start += 1
            else:
                seen.add(s[end])
            maxlen = max(maxlen, len(seen))
            end += 1

        return maxlen


        