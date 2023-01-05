from pytube import YouTube
import random

def downloadYoutube(link, res):
    yt = YouTube(link)
    if (yt.length < 600):
        yt = yt.streams.get_by_resolution(res+'p')

        try:
            youtube_video_downloaded = yt.download(output_path='videos', filename=f'youtube_{random_youtube_1}_{random_youtube_2}.mp4')
            youtube_video_downloaded
        except:
            print("Download Error")
        print("Download is completed successfully")

random_youtube_1 = random.randint(1,9999999)
random_youtube_2 = random.randint(1,9999999)

