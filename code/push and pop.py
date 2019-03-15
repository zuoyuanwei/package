# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.A = []
        self.B = []
    def push(self, node):
        # write code here
        self.A.append(node)
    def pop(self):
        # return xx
        if self.B == []:
            while self.A:
                self.B.append(self.A.pop())
            return self.B.pop()
        return self.B.pop()
