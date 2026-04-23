class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        res = 0
        count = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                count += 1
                res = max(res, count)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    count -= 1
                    l += 1
                seen.add(s[r])
                count += 1
        return res
