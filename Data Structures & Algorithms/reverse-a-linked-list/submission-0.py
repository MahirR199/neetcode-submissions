# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        if head == None:
            return head
        while head.next:
            p = head.next
            head.next = previous
            previous = head
            head = p
        head.next = previous
        return head 