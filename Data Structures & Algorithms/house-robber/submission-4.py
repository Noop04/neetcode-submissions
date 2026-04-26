class Solution:
    def rob(self, nums: List[int]) -> int:
        prevHouse = 0
        currHouse = 0
        for i in nums:
            temp = max(currHouse + i, prevHouse)
            currHouse = prevHouse
            prevHouse = temp
        return prevHouse