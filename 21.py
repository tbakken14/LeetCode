# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first = None
        out = None
        while list1 and list2:
            if not out:
                if list1.val < list2.val:
                    out = list1
                    list1 = list1.next
                else:
                    out = list2
                    list2 = list2.next
                first = out
            else:
                if list1.val < list2.val:
                    out.next = list1
                    out = out.next
                    list1 = list1.next
                else:
                    out.next = list2
                    out = out.next
                    list2 = list2.next
        if not out:
            if list1:
                return list1
            if list2:
                return list2
            return None
        if list1:
            out.next = list1
        if list2:
            out.next = list2
        if not first:
            return None
        return first
