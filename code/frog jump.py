# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number < 1:
            return 0
        else:
            return pow(2, number - 1)

