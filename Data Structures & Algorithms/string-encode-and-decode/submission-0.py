class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + str(s)
        return res



    def decode(self, s: str) -> List[str]:
        # 5#hello3#his10#
        i, j = 0, 0
        res = []
        while i < len(s):
            word = ""
            while s[i] != '#':
                i += 1
            length = int(s[j : i])
            j = i + 1
            i = i + 1 + length
            word = s[j : i]
            res.append(word)
            j = i
        return res



