#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2018/9/24 18:17
# @author  : zza
# @Email   : 740713651@qq.com

# import
import wave as we
import numpy as np
import matplotlib.pyplot as plt


def wavread(path):
    wavfile = we\
        .open(path, "rb")
    params = wavfile.getparams()
    framesra, frameswav = params[2], params[3]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav, dtype=np.short)
    datause.shape = -1, 2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return datause, time


def main():
    path ="a.wav"
    wavdata, wavtime = wavread(path)
    plt.title("Night.wav's Frames")
    plt.subplot(211)
    plt.plot(wavtime[:10**6], wavdata[0][:10**6], color='green')
    plt.subplot(212)
    k = np.gradient( wavdata[0])
    # 一秒多少个点
    point_for_one = np.sum(wavtime < 1)
    k.reshape(k/point_for_one)
    plt.plot(wavtime[:10**6], k [:10**6])
    plt.show()


main()