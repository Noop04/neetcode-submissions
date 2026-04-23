class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        idstart = 0
        idmax = 0
        idend = 0
        res = []

        
        while idend < k:
            if nums[idmax] <= nums[idend]:
                idmax = idend
            idend += 1   
        res.append(nums[idmax]) 

        
        while idend < len(nums):
            idstart += 1

            if idmax < idstart:  
                idmax = idstart
                tmp = idstart + 1
                while tmp <= idend:
                    if nums[tmp] >= nums[idmax]:
                        idmax = tmp
                    tmp += 1
            elif nums[idend] >= nums[idmax]:  
                idmax = idend

            res.append(nums[idmax])
            idend += 1
        return res
            
            



