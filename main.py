from alive_progress import alive_bar
from pytube import YouTube
import datetime
import time
import os
if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=gk0Cf3h0oOk'
    video = YouTube(url=video_url)
    video_time = datetime.datetime.fromtimestamp(float(video.length))
    video_path = video.streams.get_highest_resolution().download()
    print("VIDEO IS READY :)")
    new_year_time = datetime.datetime.strptime('2023-01-05 01:05:59','%Y-%m-%d %H:%M:%S') - datetime.datetime.now()
    start_hour = 0
    start_minute = 2
    start_second = 12
    start_time = start_hour*60*60 + start_minute*60 + start_second
    video_start_time = new_year_time.seconds - start_time
    with alive_bar(video_start_time, title='new year', length=20, bar='smooth',force_tty=True) as Bar:
        for _ in range(video_start_time):
            time.sleep(1)
            Bar()
    os.startfile(video_path)