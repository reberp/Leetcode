# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1=l1
        ptr2=l2
        carry,rem=0,0
        out=ListNode()
        head=out
        while ptr1 or ptr2 or carry:
            sum=0
            if ptr2:
                sum+=ptr2.val
            if ptr1: 
                sum+=ptr1.val
            sum+=carry
            carry=0
            val = sum
            carry=val//10
            rem=val%10
            if ptr1:
                ptr1=ptr1.next
            if ptr2:
                ptr2=ptr2.next
            head.next = ListNode(rem)
            head=head.next
        return out.next
