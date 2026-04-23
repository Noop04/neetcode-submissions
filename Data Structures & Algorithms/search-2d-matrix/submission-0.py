class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for nums in matrix:
            for i in nums:
                l,r = 0, len(nums) - 1
                if nums[r] < target:
                    break
                while l <= r:
                    m = l + ((r - l) // 2)
                    if nums[m] > target:
                        r = m - 1
                    elif nums[m] < target:
                        l = m + 1
                    if nums[m] == target:
                        return True
        return False

                