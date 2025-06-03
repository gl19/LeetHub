# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        visited = set()
        def helper(node, total, depth):
            # Base case
            if not node or (node, depth) in visited:
                return 0
            
            visited.add((node, depth))
            # Two options, continue adding to total or start new
            left_include = helper(node.left, total + node.val, depth + 1)
            left_exclude = helper(node.left, 0, 0)
            right_include = helper(node.right, total + node.val, depth + 1)
            right_exclude = helper(node.right, 0, 0)

            return ((total + node.val) == targetSum) + left_include + left_exclude + right_include + right_exclude

        return helper(root, 0, 0)