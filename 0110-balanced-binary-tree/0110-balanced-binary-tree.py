# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        def check(node):
            if not node:
                return 0

            left_height = check(node.left)
            if left_height == -1:
                return -1

            right_height = check(node.right)
            if right_height == -1:
                return -1

            diff = abs(left_height - right_height)
            
            if diff > 1:
                return -1
            else:
                return 1 + max(left_height, right_height)

        return check(root) != -1