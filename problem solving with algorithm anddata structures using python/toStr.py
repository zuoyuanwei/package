# 使用栈方法转换整数为字符串
from pythonds.basic.stack import Stack
rStack = Stack()


def toStrStack(n, base):
    convertString = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ''
    while not rStack.isEmpty():
        res += str(rStack.pop())
    return res


# 整数转换成字符串，递归，基数取余。
def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base)+convertString[n % base]


print(toStrStack(1453, 16))