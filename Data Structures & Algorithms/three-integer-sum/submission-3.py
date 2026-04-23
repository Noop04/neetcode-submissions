class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = 0
        nums = sorted(nums)
    
        while l < len(nums) - 2:
            i = l + 1
            r = len(nums) - 1
            while i < r:
                tmp = nums[l] + nums[i] + nums[r]
                if tmp > 0:
                    r -= 1
                elif tmp < 0:
                    i += 1
                else:
                    new = [nums[l], nums[i], nums[r]]
                    if new not in res:
                        res.append(new)
                    i += 1
                    r -= 1
            l += 1
        return res



            



