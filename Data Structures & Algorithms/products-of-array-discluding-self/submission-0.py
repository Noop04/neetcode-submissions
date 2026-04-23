class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # #
        # [1,2,4,6]
        # 2 4 6

        # [48,24,12,8]
        # #
        res = []
        index = 0
        while index != len(nums):
            currentIndex = 0
            product = 1
            for n in nums:
                if currentIndex == index:
                    currentIndex +=1
                    pass
                else:
                    product *= n
                    currentIndex += 1
            res.append(product)
            index += 1
        return res




        