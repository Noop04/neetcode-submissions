class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        res = nums[r]
        while l <= r:
            res = min(nums[l], nums[r], res)
            l += 1
            r -= 1
        return res