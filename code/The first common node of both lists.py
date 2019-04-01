输入两个链表，找出它们的第一个公共结点。


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        A = []
        B = []
        while pHead1:
            A.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2.val in A:
                return pHead2
            else:
                pHead2 = pHead2.next