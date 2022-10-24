# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        is_left = True
        is_right = False
        curr = head
        start = None
        prev = None
        c = 0
        while curr:
            c += 1
            if is_left:
                if c == left:
                    is_left = False
                    prev = curr
                    curr = curr.next
                else:
                    start = curr
                    curr = curr.next
            elif not is_left and not is_right:
                if c > right:
                    is_right = True
                    
                elif not start: # curr is the head
                    prev.next = curr.next
                    curr.next = head
                    head = curr
                    curr = prev.next
                else:
                    prev.next = curr.next
                    curr.next = start.next
                    start.next = curr
                    curr = prev.next
                    
                    
            else: 
                break
        return head
