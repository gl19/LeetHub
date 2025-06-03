# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        i = 0
        while head:
            values.append(head.val)
            head = head.next

        n = len(values)
        max_pair_sum = 0
        for i in range(n // 2):
            pair_sum = values[i] + values[n - i - 1]
            if pair_sum > max_pair_sum:
                max_pair_sum = pair_sum

        return max_pair_sum

