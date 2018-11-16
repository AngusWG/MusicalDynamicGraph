#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/10/28 2:28 
# @author  : zza
# @Email   : 740713651@qq.com
import call_text
import get_black_side
import mp32wav
from config import *

# 音乐转wav格式
mp32wav.server()
# 图片加黑边
get_black_side.server()
# 制作视频
call_text.main()
# 添上音频
call_text.merge_audio_video(music_path, out_vidoeo1, out_vidoeo1)
