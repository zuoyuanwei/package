# -*- coding:utf-8 -*-
# 从正数开始，和为负数则舍弃前面的数从下一个正数开始。
# 判断，当和增大时更新和，否则保留。
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum, cur_sum = -100, 0
        for i in array:
            if cur_sum <= 0:
                cur_sum = i
            else:
                cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
