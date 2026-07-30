# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # find middle 
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # reverse second half
        fast = slow.next
        slow.next = None

        prev = None

        while fast:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp

        # merge
        slow = head
        fast = prev

        while fast:
            temp1 = slow.next
            temp2 = fast.next

            slow.next = fast
            fast.next = temp1

            slow = temp1
            fast = temp2

        return