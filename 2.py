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
        head = ListNode()
        curr = head
        while l1 or l2:
            if l1 and l2:
                curr.val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                curr.val += l1.val
                l1 = l1.next
            else:
                curr.val += l2.val
                l2 = l2.next
            prev = curr
            curr = ListNode()
            prev.next = curr
            if prev.val > 9:
                prev.val = prev.val % 10
                curr.val = 1
            if not (l1 or l2) and curr.val == 0:
                prev.next = None
        return head
