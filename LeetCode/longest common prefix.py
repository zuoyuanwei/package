编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀

python两种让你拍大腿的解法，时间复杂度你想象不到，短小精悍。 
1、利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
法1：
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        B = [min(strs),max(strs)]
        a = min(len(_)for _ in B)
        count = 0
        for i in range(a):
            if B[0][i] == B[1][i]:
                count += 1
            else:
                break
        if count == 0:
            return ''
        else:
            return B[0][:count]
法2：
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        a = min(len(_)for _ in strs)
        C = []
        D = ''
        for i in range(a):
            B = []
            for j in strs:
                B.append(j[i])
            C.append(B)
        for k in C:
            if len(set(k)) == 1:
                D += k[0]
            else:
                break
        return D
两种方法时间和空间复杂度相差不大，但是代码复杂度相差较大。