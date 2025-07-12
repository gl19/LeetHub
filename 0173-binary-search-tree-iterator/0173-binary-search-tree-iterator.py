# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    
    def __init__(self, root: Optional[TreeNode]):
        self.array = []
        self.pointer = -1
        def inorder_traversal(node):
            if not node:
                return

            inorder_traversal(node.left)
            self.array.append(node.val)
            inorder_traversal(node.right)

        inorder_traversal(root)


    def next(self) -> int:
        self.pointer += 1
        return self.array[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.array)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()