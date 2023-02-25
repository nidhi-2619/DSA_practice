# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         dummy node whos next is head to avoid the edge case where , head val is equal to the val
        dummy = ListNode(next=head)
        cur = head
        ptr = dummy
        while cur:
            if cur.val==val:
                ptr.next = cur.next
            else:
                ptr = cur
            cur = cur.next
        return dummy.next       
