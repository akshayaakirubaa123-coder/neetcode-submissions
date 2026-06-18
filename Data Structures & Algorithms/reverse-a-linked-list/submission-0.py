# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head

        while curr != None:
            next = curr.next #store the next node becos pointer will be reversed 
            curr.next = prev
            prev = curr
            curr = next 
        return prev


            


        


        