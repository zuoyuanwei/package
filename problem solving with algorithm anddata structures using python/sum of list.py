# 使用递归的方法计算列表元素和。递归函数是调用自身的函数。
def listsum(num):
    if not num:
        return None
    elif len(num) == 1:
        return num[0]
    else:
        return num[0] + listsum(num[1:])

print(listsum([1,3,5,7,9]))