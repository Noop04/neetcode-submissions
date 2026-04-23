class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            tmp = numbers[l] + numbers[r]
            if tmp > target:
                # lower right
                r -= 1
            elif tmp < target:
                # increase left
                l += 1
            elif tmp == target:
                # return indexes left first
                res = [l + 1,r + 1]
                return res