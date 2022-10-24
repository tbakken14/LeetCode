# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head != None:
            if head.next != None:
                temp = head.val
                head.val = head.next.val
                head.next.val = temp
                self.swapPairs(head.next.next)
        return head
