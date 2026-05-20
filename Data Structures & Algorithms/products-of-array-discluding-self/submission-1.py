class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        res = []
        currentIndex = 0
        while currentIndex != len(nums):
            product = 1
            for i in range(len(nums)):
                if currentIndex == i:    
                    i += 1
                else: 
                    product *= nums[i]
            res.append(product)
            currentIndex += 1
        return res









        