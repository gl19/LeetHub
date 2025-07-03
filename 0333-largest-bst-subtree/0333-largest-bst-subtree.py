# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_count = 0
        
        def helper(node):
            if not node:
                # is_bst, size, min_val, max_val
                return True, 0, float('inf'), float('-inf')
            
            left_is_bst, left_size, left_min, left_max = helper(node.left)
            right_is_bst, right_size, right_min, right_max = helper(node.right)
            
            # Check if current subtree is BST
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                self.max_count = max(self.max_count, size)
                return True, size, min(node.val, left_min), max(node.val, right_max)
            else:
                return False, 0, 0, 0
        
        helper(root)
        return self.max_count

            
