# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 1)]
        max_total = float('-inf')
        max_level = 0

        total = 0
        last_level = 1
        while len(queue) > 0:
            node, level = queue.pop(0)
            if level != last_level:
                if total > max_total:
                    max_total = total
                    max_level = last_level

                last_level = level
                total = 0

            total += node.val
            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        if total > max_total:
            return last_level

        return max_level

            


        return max_level


        