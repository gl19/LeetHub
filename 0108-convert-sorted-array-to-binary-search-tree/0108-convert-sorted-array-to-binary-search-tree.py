# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(node, left, right):
            if len(left) == 0 and len(right) == 0:
                return node

            if len(left) > 0:
                mid = len(left) // 2
                node.left = helper(TreeNode(left[mid], None, None), left[:mid], left[mid + 1:])

            if len(right) > 0:
                mid = len(right) // 2
                node.right = helper(TreeNode(right[mid], None, None), right[:mid], right[mid + 1:])

            return node

        
        mid = len(nums) // 2
        root = TreeNode(nums[mid], None, None)
        return helper(root, nums[:mid], nums[mid + 1:])

        