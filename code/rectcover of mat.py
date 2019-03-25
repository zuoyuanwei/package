# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        else:
            f = [None] * number
            f[0] = 1
            f[1] = 2
            for i in range(2, number):
                f[i] = f[i - 1] + f[i - 2]
        a = f[number - 1]
        return a
