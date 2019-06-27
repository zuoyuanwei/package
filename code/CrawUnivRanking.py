# 全国大学排名爬虫。
import requests
from bs4 import BeautifulSoup
allUniv = []
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''

def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)
    allUniv.reverse()   # 例题要求输出倒数的n个大学
    # print(allUniv, len(allUniv))
    # return allUnivList
    # print(allUnivList, len(allUnivList))

# 对齐，填充。
def printUnivList(num):
    print('{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}'.format(chr(12288), '排名', '学校名称', '省市', '总分', '培养规模'))
    for i in range(num):
        u = allUniv[i]
        print('{1:^4}{2:{0}^10}{3:{0}^5}{4:{0}^8}{5:{0}^10}'.format(chr(12288), u[0], u[1], u[2], eval(u[3]), u[6]))

def main(num):
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHtmlText(url)
    soup = BeautifulSoup(html, 'html.parser')
    fillUnivList(soup)
    printUnivList(num)

main(50)
