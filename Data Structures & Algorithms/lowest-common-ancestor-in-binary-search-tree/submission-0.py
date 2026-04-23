# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        pval = p.val
        qval = q.val
        if not root:
            return none
        while True:
            if pval > curr.val and qval > curr.val:
                curr = curr.right
            elif pval < curr.val and qval < curr.val:
                curr = curr.left
            else:
                return curr
            