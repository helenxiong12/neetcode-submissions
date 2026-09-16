class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            pref = len(s)
            encoding += str(pref) + ":"
            encoding += s
        print("encode", encoding)
        return encoding
    # 5:Hello5:World
    def decode(self, s: str) -> List[str]:
        idx = 0
        words = []
        while idx < len(s):
            # parse len
            start_idx = idx
            end_idx = s[idx:].find(':') + idx
            # print("parselen", start_idx, end_idx, s[start_idx:end_idx])
            strlen = int(s[start_idx:end_idx])

            start = end_idx + 1
            end = start + strlen
            word = s[start:end]
            words.append(word)
            idx = end

            # print(strlen, word, idx)
        return words
