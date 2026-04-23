class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
            myset = set(nums)
            longest = 0

            for num in myset:
                if num - 1 not in myset:
                    length = 1
                    current = num + 1
                    while current in myset:
                        length += 1
                        current += 1
                # if num - 1 exists => pass
                    longest = max(length, longest)
            return longest



                
            
            