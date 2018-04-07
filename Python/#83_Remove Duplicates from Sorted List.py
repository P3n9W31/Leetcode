# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        l1_head = ListNode(0)
        l1_head.next = head
        buff = [head.val]
        
        while head.next:
            if head.next.val in buff:
                head.next = head.next.next
            else:
                buff.append(head.next.val)
                head = head.next
            
        return l1_head.next