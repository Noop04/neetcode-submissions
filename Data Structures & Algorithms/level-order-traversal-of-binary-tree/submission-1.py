# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0
        if not root:
            return []
        

        def levels(level, node):
            if not node:
                return None
            if len(res) == level:
                res.append([])
            res[level].append(node.val)

            levels(level + 1, node.left)
            levels(level + 1, node.right)

        levels(0, root)
        return res

        
    
    

