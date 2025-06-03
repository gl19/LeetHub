# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solution 1
        def iterative():
            prev = None
            cur = head
            while cur:
                cur_next = cur.next
                cur.next = prev
                prev = cur
                cur = cur_next
                
            return prev

        # solution 2
        def recursive(cur):
            if cur is None or cur.next is None:
                return cur

            node = recursive(cur.next)
            cur.next.next = cur
            cur.next = None
            return node

        return recursive(head)