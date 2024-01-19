# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=head
        r=head
        if not head:
            return False
        if not head.next:
            return False
        if head.next:
            while r.next and r.next.next:
                r=r.next.next
                l=l.next
                if r==l:
                    return True
        return False