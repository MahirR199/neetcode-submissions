# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = (l1.val + l2.val)%10
        carry = (l1.val+l2.val)//10
        head = l1
        l1.val = sum
        while l1.next and l2.next:
            l1=l1.next
            l2=l2.next
            sum = (l1.val + l2.val+carry)%10
            carry = (l1.val+l2.val+carry)//10
            l1.val = sum
            
        while l1.next:
            l1 = l1.next
            sum = (l1.val+carry)%10
            carry = (l1.val+carry)//10
            l1.val = sum
        while l2.next:
            l2 = l2.next
            sum = (l2.val+carry)%10
            carry = (l2.val+carry)//10
            newNode = ListNode()
            newNode.val = sum
            l1.next = newNode
            l1 = l1.next
        if carry > 0:
            newNode = ListNode()
            newNode.val = carry
            l1.next = newNode

        return head
        