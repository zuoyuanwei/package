from bs4 import BeautifulSoup
from urllib.request import urlopen

step1:read the original heml
# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

step2:find something in the html by bs4
soup = BeautifulSoup(html, features='lxml')
print(soup.h1)	# using soup.h1 print the word between<h1>
print('\n', soup.p)	# print paragram

step3:
all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)	# print link