from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort anagrams, zip with indexes
        # group words by index 
        # for each word: sort word
        # start a dictionary
        # if sorted in dictionary, append word to list 
        # return dictionary 
        def count_chars(s) -> str:
            char_count = [0] * 26
            for c in s:
                # calculate the index of the character
                idx = ord(c) - ord('a')
                char_count[idx] += 1 # increment the index
            # missed edge case where using "".join led to bug
            return " ".join([str(c) for c in char_count])

        res = defaultdict(list)
        for s in strs:
            # sorted_s = "".join(sorted(strs[i]))
            # res[sorted_s].append(strs[i])
            print(count_chars(s))
            res[count_chars(s)].append(s)
        return list(res.values())

    