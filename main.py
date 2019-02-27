import subprocess
import json
import os
import threading
import queue
import asyncio
from pytest import approx

def convert_video(Q,file):
    if not Q.empty():
        async def covert_720p():
            os.system('ffmpeg -i ' + file + ' -r 30 -b 2M -s 1280x720 ' + file + '_720.mp4')
            print(threading.currentThread())
            return '720P covert successfully'

        async def covert_480p():
            os.system('ffmpeg -i ' + file + ' -r 30 -b 1M -s 720x480 ' + file + '_480.mp4')
            print(threading.currentThread())
            return '480P covert successfully'

        coroutine1 = covert_720p()
        coroutine2 = covert_480p()

        thread_list = [
            asyncio.ensure_future(coroutine1),
            asyncio.ensure_future(coroutine2),
        ]

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(thread_list))

        for thread in thread_list:
            print('thread: ', thread.result())

def ffprobe(file) -> dict:
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                    file])
    return json.loads(meta)

def main():
    Q = queue.Queue()
    path = 'D:\EC500\Exercise2'
    for file in os.listdir(path):
        if file.endswith('.mp4'):
            Q.put(file)
    convert_video(Q,file)
    ffprobe(file)

def test_duration():
    fnin = 'videoplayback.mp4'
    fnout = 'videoplayback.mp4_480.mp4'

    orig_meta = ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    meta_480 = ffprobe(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])

    assert orig_duration == approx(duration_480)



if __name__ == '__main__':
   main()
