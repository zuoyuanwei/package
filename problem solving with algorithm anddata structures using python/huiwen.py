# 使用双向列表解决回文字符串会很容易，将字符串从尾部存入队列，deque首部存放字符串第一个
# 字符，尾部保存最后一个字符。我们可以直接删除比较首尾字符，只有当他们一致时继续，最终
# 用完字符或者只剩一个字符，这两种情况都是回文字符串。
from pythonds.basic.deque import Deque


def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual


print(palchecker('radar'))
print(palchecker('lsdkjfskf'))