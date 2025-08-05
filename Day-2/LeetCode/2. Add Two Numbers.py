"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        returnList = ListNode()
        list1 = l1
        list2 = l2
        
        num1 = ""
        num2 = ""

        while list1 != None or list2 != None:
            if list1 != None:
                num1 = num1 + str(list1.val)
                list1 = list1.next

            if list2 != None:
                num2 = num2 + str(list2.val)
                list2 = list2.next

        num1 = num1[::-1]
        num2 = num2[::-1]

        res = int(num1) + int(num2)
        res = str(res)

        for c in res:
            returnList.val = int(c)
            tmp = returnList
            returnList = ListNode()
            returnList.next = tmp

        return returnList.next