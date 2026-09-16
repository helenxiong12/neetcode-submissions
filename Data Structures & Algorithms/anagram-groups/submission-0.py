from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort anagrams, zip with indexes
        # group words by index 
        # for each word: sort word
        # start a dictionary
        # if sorted in dictionary, append word to list 
        # return dictionary 
        res = defaultdict(list)
        for i in range(len(strs)):
            sorted_s = "".join(sorted(strs[i]))
            # print(sorted_s, i)
            res[sorted_s].append(strs[i])
        return list(res.values())

    