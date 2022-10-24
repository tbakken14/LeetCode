# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        for i in range(1,n):
            if curr.next == None:
                return None
            curr = curr.next
        d = head
        last = None
        while curr.next != None:
            curr = curr.next
            last = d
            d = d.next
        if not last:
            return head.next
        last.next = d.next
        return head
