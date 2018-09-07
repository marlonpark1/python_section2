from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 403 Error 발생 방지 코드
opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote
print(url)

res = req.urlopen(url)
savePath = "C:\\imagedown\\"  # C:/imagedown/ 이미지 다운로드 폴더

try:
    if not os.path.isdir(savePath):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != e.EEXIST:
        print("폴더만들기 실패!")
        raise  # 파이썬 에러발생 코드

soup = BeautifulSoup(res, "html.parser")

imge_list = soup.select("ul.slides")[0]

for i, e in enumerate(imge_list, 1):
    with open(savePath+'test_'+str(i)+'.txt', 'wt') as f:
        f.write(e.select_one("h4.block_title > a").string)
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'], fullFileName)

print("다운로드 완료")
