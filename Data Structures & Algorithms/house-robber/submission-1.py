class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev2 = 0
        prev1 = 0
        for i in range(len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        return prev1