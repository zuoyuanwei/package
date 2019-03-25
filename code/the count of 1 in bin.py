# -*- coding:utf-8 -*-
# 如果n大于0，直接计算即可，如果n小于0，计算2的32次方加上n的结果中1的个数。
class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n).replace("0b","").count("1") if n>=0 else bin(2**32+n).replace("0b","").count("1")