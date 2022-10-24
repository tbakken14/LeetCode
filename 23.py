# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        for l in lists:
            if not l:
                lists.remove(l)
        if len(lists) < 1:
            return None

        while len(lists) > 1:
            a = lists.pop(0)
            b = lists.pop(0)
            lists.append(self.merge(a, b))
        return lists[0]
        
    def merge(self, n1, n2):
        h = None 
        while n1 and n2:
            if n1.val < n2.val:
                if not h:
                    h = n1
                    curr = h
                else:
                    curr.next = n1
                    curr = curr.next
                n1 = n1.next
            elif n1.val > n2.val:
                if not h:
                    h = n2
                    curr = h
                else:
                    curr.next = n2
                    curr = curr.next
                n2 = n2.next
            else:
                if not h:
                    h = n1
                    curr = h
                    n1 = n1.next
                    curr.next = n2
                    curr = curr.next
                    n2 = n2.next
                else:
                    curr.next = n1
                    curr = curr.next
                    n1 = n1.next
                    curr.next = n2
                    curr = curr.next
                    n2 = n2.next
        if n1:
            if not h:
                h = n1
            else:
                curr.next = n1
        elif n2:
            if not h:
                h = n2
            else:
                curr.next = n2
        return h
