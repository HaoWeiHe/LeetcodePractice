# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = 0 
        c = -1
        d = head
        while d:
            c += 1
            d = d.next
            
        
        while head:
            res += head.val<< c
        
            c -=1
            head = head.next
        return res