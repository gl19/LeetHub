# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(int)
        queue = [(root, 1)]
        while len(queue) > 0:
            node, level = queue.pop(0)
            levels[level] += node.val
            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        max_sum = float('-inf')
        max_level = 0
        for level in levels.keys():
            if levels[level] > max_sum:
                max_level = level
                max_sum = levels[level]

        return max_level


        