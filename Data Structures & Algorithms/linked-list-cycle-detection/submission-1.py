# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = head
        b = head
        while a and b and b.next and b.next.next:
            a = a.next
            b = b.next
            b = b.next.next
            if b == a:
                    return True
        return False