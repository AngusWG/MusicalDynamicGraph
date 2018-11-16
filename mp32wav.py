#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/9/24 16:28 
# @author  : zza
# @Email   : 740713651@qq.com
import os

from pydub import AudioSegment


def trans_mp3_to_wav(file):
    song = AudioSegment.from_mp3(file)
    song.export(file[:-3] + "wav", format="wav")


def server():
    _dir = "music"
    files = os.listdir(_dir)
    for file in files:
        if file.endswith(".mp3") and file[:-3] + "wav" not in files:
            print(os.path.join(_dir, file, "转换为.wav格式成功"))
            trans_mp3_to_wav(os.path.join(_dir, file))


if __name__ == '__main__':
    server()
    pass
