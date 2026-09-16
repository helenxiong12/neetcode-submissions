class Solution:

    def encode(self, strs: List[str]) -> str:
        # 3,4,5:words...
        # get length of strings, join with ",", concat words and join with lengths
        lens = []
        concat_strs = ""
        for s in strs:
            lens.append(len(s))
            concat_strs += s
        return ",".join([str(l) for l in lens]) + ":" + concat_strs

    def decode(self, s: str) -> List[str]:
        # separate lengths array from words array
        lens_str = s[:s.index(':')]
        strs = []
        if len(lens_str) > 0:
            lens = [int(l) for l in lens_str.split(",")]
            concat_str = s[s.index(':')+1:]
            idx = 0
            for l in lens:
                strs.append(concat_str[idx:idx+l])
                idx = idx+l
        return strs

