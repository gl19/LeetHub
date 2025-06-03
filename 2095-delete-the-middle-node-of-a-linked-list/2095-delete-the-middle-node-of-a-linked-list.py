# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
            
        prev_turtle = None
        turtle = head
        hare = head
        turtle_move = False
        while hare:
            hare = hare.next
            if turtle_move:
                prev_turtle = turtle
                turtle = turtle.next
                turtle_move = False
            else:
                turtle_move = True

        
        prev_turtle.next = turtle.next

        return head
