# 我们有3种物品，他们的重量和价格分别是10, 20, 30 kg和60, 100, 120。背包总容量50，求存储物品价值最大。
import numpy as np


def solve(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros((totalLength+1, totalWeight+1), dtype=np.int32)
    for i in range(1, totalLength+1):
        for j in range(1, totalWeight+1):
            if wlist[i] <= j:
                resArr[i, j] = max(resArr[i-1, j-wlist[i]]+vlist[i], resArr[i-1, j])
            else:
                resArr[i, j] = resArr[i-1, j]
    return resArr[-1, -1]


if __name__ == '__main__':
    v = [0, 60, 100, 120]
    w = [0, 10, 20, 30]
    weight = 50
    n = 3
    result = solve(v, w, weight, n)
    print(result)
