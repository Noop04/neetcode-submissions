class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        count = 0
        seen = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                count += 1
                seen.add(s[r])
                r += 1
                res = max(res, count)
            else: # s[r] is in seen pop from left
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    count -= 1
        return res

