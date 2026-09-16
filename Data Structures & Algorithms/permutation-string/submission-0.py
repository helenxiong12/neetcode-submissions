class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isSubset(s1_set:List, s2_set:List) -> bool:
            for c in range(26):
                if s1_set[c] != s2_set[c]:
                    return False
            return True
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        seen_s1 = [0 for _ in range(26)]
        seen_s2 = [0 for _ in range(26)]
        for i in range(n1):
            seen_s1[ord(s1[i]) - ord('a')] += 1
            seen_s2[ord(s2[i]) - ord('a')] += 1
        if seen_s1 == seen_s2:
            return True

        for i in range(n1, n2):
            seen_s2[ord(s2[i]) - ord('a')] += 1
            seen_s2[ord(s2[i-n1]) - ord('a')] -= 1
            if isSubset(seen_s1, seen_s2):
                return True
        return False








        