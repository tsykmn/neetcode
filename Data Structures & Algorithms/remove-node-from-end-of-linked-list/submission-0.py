# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        left = head
        right = head

        while n != 0:
            right = right.next
            n -= 1
        
        while right:
            curr.next = left
            curr = curr.next
            left, right = left.next, right.next
        
        curr.next = left.next

        return res.next
        