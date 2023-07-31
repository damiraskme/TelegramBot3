from pytube import YouTube
import random

def downloadYoutube(link, id):
    yt = YouTube(link.strip())
    if (yt.length < 600):
        yt = yt.streams.get_by_resolution("720p")
        try:
            youtube_video_downloaded = yt.download(output_path='videos', filename=f'youtube_for_{id}.mp4')
            youtube_video_downloaded
            print("Download is completed successfully")
        except:
            print("Download Error")
        
def getTitle(link):
    yt = YouTube(link.strip())
    title = yt.title
    return title

def downloadYoutubemp3(link, id):
    yt = YouTube(link.strip())
    if (yt.length < 600):
        yt = yt.streams.filter(only_audio=True).first()
        try:
            youtube_video_downloaded = yt.download(output_path='videos', filename=f'youtube_for_{id}.mp3')
            youtube_video_downloaded
            print("Download is completed successfully")
        except:
            print("Download Error")

