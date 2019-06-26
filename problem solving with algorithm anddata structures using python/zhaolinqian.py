# 动态规划找零钱问题。
# 第一个方法低效，存在重复计算。
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins
# 第二个方法使用递推代替递归，每次保存计算结果避免重复计算。
def recDC(coinValueList, change, knowResults):
    minCoins = change
    if change in coinValueList:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:   # 与第一个方法的不同点，先查找结果是否已知，如果已知直接使用而不是重复计算。
        return knowResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i, knowResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change] = minCoins
    return minCoins

# 用动态规划解决找零问题
def dpMakeChange(coinValuelist, change, minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValuelist if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
        minCoins[cents] = coinCount
    return minCoins[change]
# 跟踪最小硬币数方案。
def dpMakeChange1(coinValuelist, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValuelist if c <= cents]:
            if minCoins[cents-j] +1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]
def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin
def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)
    print('Making change for', amnt, 'requires')
    print(dpMakeChange1(clist, amnt, coinCount, coinsUsed), 'coins')
    print('They are:')
    printCoins(coinsUsed, amnt)
    print('The used list is as follows:')
    print(coinsUsed)
main()
print(dpMakeChange([1,5,10,25], 63, [0]*64))