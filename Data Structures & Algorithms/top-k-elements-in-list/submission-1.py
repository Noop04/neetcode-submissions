class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            if n in res:
                res[n] += 1
            else:
                res[n] = 1
        
        ans = []
        while k > 0:
            most = 0
            mostKey = None
            for key in res:
                if res[key] > most:
                    most = res[key]
                    mostKey = key
            ans.append(mostKey)
            del res[mostKey]
            k -= 1
        return ans