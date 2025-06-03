# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        def helper(node, direction, length):
            nonlocal max_length

            if not node:
                return

            if direction == 'right':
                helper(node.left, 'left', length + 1)
                helper(node.right, 'right', 1)
            elif direction == 'left':
                helper(node.right, 'right', length + 1)
                helper(node.left, 'left', 1)

            if length > max_length:
                max_length = length


        helper(root.left, 'left', 1)
        helper(root.right, 'right', 1)
        return max_length


            
