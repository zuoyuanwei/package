给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        A = []
        while pHead.next:
            A.append(pHead.val)
            if pHead.next.val in A:
                return pHead.next
            else:
                pHead = pHead.next
        return None