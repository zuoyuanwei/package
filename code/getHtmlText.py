import requests
def getHtmlText():
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()    # 如果状态不是200，引发异常。
        r.encoding = 'utf-8'    # 强制使用utf-8编码，可显示中文。
        return r.text
    except:
        return None
url = 'http://www.baidu.com'    # url链接必须采用HTTP或HTTPS方式访问。
print(getHtmlText())