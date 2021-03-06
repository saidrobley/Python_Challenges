# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        res = ListNode(-1)
        p = l1
        q = l2
        carry = 0
        curr = res
        while p != None or q != None:
            if p != None:
                x = p.val
            elif p == None:
                x = 0
            if q != None:
                y = q.val
            elif q == None:
                y = 0
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return res.next
