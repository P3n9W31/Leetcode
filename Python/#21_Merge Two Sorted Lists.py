# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        l3 = head
        
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next
            else:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
        if l1:
            while l1:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
        if l2:
            while l2:
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next
        return head.next