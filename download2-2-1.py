import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgURL = "http://post.phinf.naver.net/20160703_160/linakim97_1467531966225KC943_JPEG/mug_obj_201607031646063616.jpg"
htmlURL = "http://google.com"

savePath1 = "c:/test1.jpg"
savePath2 = "c:/index.html"

dw.urlretrieve(imgURL, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
