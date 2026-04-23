class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x1 = x2 = 0
        total = []

        while x1 < len(nums1) or x2 < len(nums2):
            if x2 == len(nums2) or (x1 < len(nums1) and nums1[x1] <= nums2[x2]):
                total.append(nums1[x1])
                x1 += 1
            else:
                total.append(nums2[x2])
                x2 += 1

        n = len(total)
        mid = n // 2

        if n % 2 == 0:
            return (total[mid - 1] + total[mid]) / 2
        else:
            return total[mid]
