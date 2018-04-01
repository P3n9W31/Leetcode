# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        buff = 0
        head = ListNode(0)
        l_sum = head
        
        
        while l1 and l2:    
            l_sum.next = ListNode((l1.val + l2.val + buff)%10)
            buff = (l1.val + l2.val + buff)//10
            l1 = l1.next
            l2 = l2.next
            l_sum = l_sum.next
                
        if l1:
            while l1:
                l_sum.next = ListNode((l1.val + buff)%10)
                buff = (l1.val + buff)//10
                l1 = l1.next
                l_sum = l_sum.next
                
        if l2:
            while l2:
                l_sum.next = ListNode((l2.val + buff)%10)
                buff = (l2.val + buff)//10
                l2 = l2.next
                l_sum = l_sum.next

                
        
        if buff != 0:
            l_sum.next = ListNode(buff)

        return head.next