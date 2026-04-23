class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAABABBBAB
        # AAA CC BB AA BB AC
        if not s:
            return 0
        
        l =  0
        res = 0
        count = {}
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, right - l + 1)

        return res