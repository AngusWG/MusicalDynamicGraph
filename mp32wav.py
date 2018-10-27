#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/9/24 16:28 
# @author  : zza
# @Email   : 740713651@qq.com
import os

from pydub import AudioSegment  ###需要安装pydub、ffmpeg


def trans_mp3_to_wav(file):
    song = AudioSegment.from_mp3(file)
    song.export(file[:-3] + "wav", format="wav")


def server():
    files = os.listdir(".")
    for file in files:
        if file.endswith(".mp3") and file[:-3] + "wav" not in files:
            print(file)
            trans_mp3_to_wav(file)


if __name__ == '__main__':
    server()
    pass
