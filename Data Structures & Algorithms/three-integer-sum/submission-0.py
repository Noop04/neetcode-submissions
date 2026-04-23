class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l = 0

        while l < len(nums) - 2:
            inside = l + 1
            r = len(nums) - 1
            while inside < r:
                tmp = nums[l] + nums[inside] + nums[r]
                if tmp > 0:
                    r -= 1
                elif tmp < 0:
                    inside += 1
                else:
                    three = [nums[l], nums[inside], nums[r]]
                    if three not in res:
                         res.append([nums[l], nums[inside], nums[r]])
                    inside += 1
                    r -= 1
            l += 1
        return res


            



