# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return []
        while head:
            if head.val != val:
                l1_head = head
                break
            else:
                head = head.next
        if head != None:
            while head.next:
                if head.next.val == val:
                    head.next = head.next.next
                else:
                    head = head.next
            return l1_head
        else:
            return []