import pytube
import os
import subprocess

# 다운 받을 동영상 URL 지정
down_url = input("다운받을 주소 입력")

yt = pytube.YouTube(down_url)
video = yt.streams.all()

# print('video', video)

for i in range(len(video)):  # range(6)
    print(i, ',', video[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

down_dir = "C:\youtube"

video[cNum].download(down_dir)

newFileName = input("변환할 mp3 파일명은?")
oriFileName = video[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
                os.path.join(down_dir, oriFileName),
                os.path.join(down_dir, newFileName)])

print("동영상 다운로드 및 mp3 변환 완료!")
