from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://www.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')

# print('soup', soup.prettify())

hotissue = soup.find_all("a", tabindex="-1")

for i, e in enumerate(hotissue, 1):
    print(i, e.string, 'link',  e.get('href'))
