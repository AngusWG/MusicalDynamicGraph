import os
import wave as we
import numpy as np
import ffmpy
import cv2

from config import *

music_path.replace(".mp3", ".wav")


def get_imgs(path="pic"):
    import os
    s = os.listdir(path)
    return [os.path.join(path, i) for i in s]


def made_video(datause, time):
    print("start made_video")
    img_path = get_imgs()
    videoWriter = cv2.VideoWriter(out_vidoeo1, cv2.VideoWriter_fourcc(*'MJPG'), pics_for_1s, (height, width))

    pic_index = 0
    for i in range(len(datause)):
        if i == 0:
            continue
        if i == len(datause) - 1:
            break
        if datause[i] > datause[i - 1] and datause[i] > datause[i + 1]:
            print(i)
            pic_index = pic_index + 1
        img = cv2.imread(img_path[pic_index % len(img_path)])
        img = cv2.resize(img, (height, width))
        videoWriter.write(img)
        print(i, len(datause))
    videoWriter.release()
    print("\nmade_video over")



def merge_audio_video(wav_file_name: str, avi_file_name: str, audio_video_file_name: str) -> str or None:
    '''
    给视频加声音
    1. takes names of .wav and .avi file
    2. merges them into one file
    '''
    if os.path.getsize(audio_video_file_name):
        os.remove(audio_video_file_name)
    try:
        ffmpy.FFmpeg(inputs={wav_file_name: None, avi_file_name: None}, outputs={audio_video_file_name: None}).run()
        return audio_video_file_name
    except Exception as e:
        print(str(e))
        return None


def wavread():
    wavfile = we.open(music_path, "rb")
    params = wavfile.getparams()
    framesra, frameswav = params[2], params[3]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav, dtype=np.short)
    datause.shape = -1, 2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0 / framesra)

    缩小 = int(framesra / pics_for_1s)
    time = time[:-1 * (len(time) % 缩小)]
    time = np.array(time).reshape(-1, 缩小)
    time = np.mean(time, axis=1)

    datause = datause[0]
    datause = datause[:-1 * (len(datause) % 缩小)]
    datause = np.array(datause).reshape(-1, 缩小)
    datause = np.mean(datause, axis=1)

    # # 求导
    # datause = np.gradient(datause)
    return datause, time


def main():
    datause, time = wavread()
    made_video(datause, time)


if __name__ == '__main__':
    main()
    # test()
    # 音频视屏融合
    merge_audio_video(music_path, out_vidoeo1, out_vidoeo2)
    pass
