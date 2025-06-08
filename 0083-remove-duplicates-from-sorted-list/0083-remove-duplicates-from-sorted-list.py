# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        start_num_node = head
        while node:
            if node.val != start_num_node.val:
                if start_num_node:
                    start_num_node.next = node

                start_num_node = node

            node = node.next
            
        if start_num_node is not None:
            start_num_node.next = None

        return head