# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def helper(node, total, path):
            nonlocal targetSum, paths
            total += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if total == targetSum:
                    paths.append(path.copy())

                return

            if node.left:
                helper(node.left, total, path)
                path.pop()
                
            
            if node.right:
                helper(node.right, total, path)
                path.pop()

        if root:
            helper(root, 0, [])
            
        return paths
                
            