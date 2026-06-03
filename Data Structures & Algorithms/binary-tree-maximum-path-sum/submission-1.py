# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        m = root.val

        def dfs(node):
            if not node:
                return 0
            nonlocal m
            
            left = dfs(node.left)
            right = dfs(node.right)
            lmax = max(left, 0)
            rmax = max(right, 0)
            pathVal = node.val + rmax + lmax
            m = max(m, pathVal)
            return node.val + max(lmax, rmax)

        dfs(root)
        return m
