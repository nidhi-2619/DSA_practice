# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # point to the second node
        curr = head
        while curr:
            ptr = curr.next 
            curr.next = prev
            prev = curr
            curr = ptr
        return prev    
            
        
