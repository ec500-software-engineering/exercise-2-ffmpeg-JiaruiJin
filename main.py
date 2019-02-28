import os
import threading
import queue
import asyncio


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


def main():
    Q = queue.Queue()
    path = 'D:\EC500\Exercise2'
    for file in os.listdir(path):
        if file.endswith('.mp4'):
            Q.put(file)
    convert_video(Q,file)


if __name__ == '__main__':
   main()
