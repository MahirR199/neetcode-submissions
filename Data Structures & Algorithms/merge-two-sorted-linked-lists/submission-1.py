# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x = list1
        y = list2
        #if empty x
        if not x:
            return y
        #if empty y
        if not y:
            return x
        
        #if value of head of x is > head of y make y's list x
        if x.val>y.val:
            x, y = y, x
        
        head = x
        #while y has next number
        while y:
            #if x.next is not none: 
                #then compare y.val with x.next
            if x.next:
                if x.next.val>y.val:
                    #placehold x.next
                    z = x.next
                    x.next = y
                    y = y.next
                    x.next.next = z
                    x = x.next
                else:
                    x = x.next
                    
                #else make the rest of y the next of x
            else:
                x.next = y
                return head
        return head



        
        # a = list1
        # b = list2
        # if a == None:
        #     return b
        # if b == None:
        #     return a
        # if a.val>b.val:
        #     a,b = b,a
        # head = a
        
        # while a.next and b:
        #     if b.val<a.next.val:
        #         c = a.next
        #         a.next = b
        #         a.next.next = c
        #         b = b.next
        #         a = a.next
        #     else:
        #         a = a.next
        
        # if a.next == None and b!=None:
        #     a.next = b
        #     return head
        # return head

