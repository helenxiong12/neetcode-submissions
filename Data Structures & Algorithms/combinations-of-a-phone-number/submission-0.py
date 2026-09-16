class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        res = [""]
        mapping = {'2' : "abc", '3' : "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz" }
        for d in digits:
            res = [r + c for c in mapping[d] for r in res]
        return res


        