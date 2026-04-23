# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start = ListNode()

        nums = []

        curr = head
        # get all vals from link list -> array
        while curr:
            nums.append(curr.val)
            curr = curr.next
        res = []
        l , r = 0, len(nums) - 1
        while l <= r:
            res.append(nums[l])
            res.append(nums[r])
            l += 1
            r -= 1

        curr = head
        index = 0
        while curr:
            curr.val = res[index]
            curr = curr.next
            index += 1 


