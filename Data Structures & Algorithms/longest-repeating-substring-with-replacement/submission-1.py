class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = collections.defaultdict(int)
        maxc = 0
        maxl = 0
        start = 0
        for i in range(len(s)):
            chars[s[i]] += 1
            maxc = max(maxc, chars[s[i]])

            while (i - start + 1) - maxc > k:
                chars[s[start]] -= 1
                start += 1
            maxl = max(maxl, i - start + 1)
        return maxl




        