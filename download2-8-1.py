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

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
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

imge_list = soup.select("div.img_area > a.thumb._thumb > img")

for i, img_source in enumerate(imge_list, 1):
    # print(i, img_source['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(img_source['data-source'], fullFileName)

print("다운로드 완료")
