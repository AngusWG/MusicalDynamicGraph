# import wave
# import numpy as np
# import matplotlib.pyplot as plt
#
# # https://blog.csdn.net/qq_39516859/article/details/79903710
# filepath = "a.wav"
# f = wave.open(filepath, 'rb')
#
# params = f.getparams()
# nchannels, sampwidth, framerate, nframes = params[:4]
# strData = f.readframes(nframes)
# w = np.fromstring(strData, dtype=np.int16)
# w = w * 1.0 / (max(abs(w)))
# w = np.reshape(w, [nframes, nchannels])
# time = np.arange(0, nframes) * (1.0 / framerate)
#
# plt.figure()
# plt.subplot(5, 1, 1)
# plt.plot(time, w[:, 0])
# plt.xlabel("Time(s)")
# plt.title("First Channel")
# plt.savefig("a.png")
# plt.close()

import wave as we
import numpy as np
import ffmpy
import matplotlib.pyplot as plt
import cv2

IMAGE_SIZE = 400
height = IMAGE_SIZE * 4
width = IMAGE_SIZE * 3


def get_imgs(path="pic"):
    import os
    s = os.listdir(path)
    return [os.path.join(path, i) for i in s]


def made_video(t, k):
    img_path = get_imgs()
    videoWriter = cv2.VideoWriter('video\out1.avi', cv2.VideoWriter_fourcc(*'MJPG'), 3, (400 * 4, 400 * 3))
    img_path = img_path * 3
    for path in img_path:
        print(path)
        img = cv2.imread(path)
        img = cv2.resize(img, (400 * 4, 400 * 3))
        videoWriter.write(img)
    videoWriter.release()


def merge_audio_video(wav_file_name: str, avi_file_name: str, audio_video_file_name: str) -> str or None:
    '''
    给视频加声音
    1. takes names of .wav and .avi file
    2. merges them into one file
    '''

    try:
        ffmpy.FFmpeg(inputs={wav_file_name: None, avi_file_name: None}, outputs={audio_video_file_name: None}).run()
        return audio_video_file_name
    except Exception as e:
        print(str(e))
        return None


def wavread(path):
    wavfile = we.open(path, "rb")
    params = wavfile.getparams()
    framesra, frameswav = params[2], params[3]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav, dtype=np.short)
    # datause.shape = -1, 2
    # datause = datause.T
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return time, datause


def main():
    path = "a.wav"
    x, y = wavread(path)
    k = np.gradient(y)

    # print(np.max(x))
    # for i in range(len(x)):
    #     print(int(x[i]), y[i], k[i])
    #     x = np.array(x[:len(x) % 1 * -1]).reshape(int(len(x) / 1), i)
    #     x = np.mean(x, axis=0)
    # print(x, y, k)
    # made_video(x, k)


if __name__ == '__main__':
    main()
    # test()
    # 音频视屏融合
    # merge_audio_video("a.wav", "video\out1.avi", "video\out2.avi")
    pass
