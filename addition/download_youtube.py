from pytube import YouTube
import os
import logging

def downloadYoutube(link, id):
    yt = YouTube(link.strip())
    if (yt.length < 600):
        yt = yt.streams.get_by_resolution("720p")
        try:
            youtube_video_downloaded = yt.download(output_path='addition/videos', filename=f'youtube_for_{id}.mp4')
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
            youtube_video_downloaded = yt.download(output_path='addition/videos', filename=f'youtube_for_{id}.mp3')
            youtube_video_downloaded
            print("Download is completed successfully")
        except:
            print("Download Error")

def getYoutubeLength(link):
    yt = YouTube(link.strip())
    length = yt.length
    if (length <= 1800):
        parts = (length // 600)
        for i in range(0, parts*600, 600):
            yt.streams.filter(progressive=True, file_extension="mp4",).first().download(
                output_path="addition/videos",
                filename=f"{getTitle(link)+str(i+1)}",
                skip_existing=True,
                start = i,
                end=i+600
            )

def deleteYoutube(id: str, ext: str):
    try:
        if (os.path.isfile(f"addition/videos/youtube_for_{id}.{ext}")):
            os.remove(f"addition/videos/youtube_for_{id}.{ext}")
            logging.info("File deleted")
    except FileNotFoundError:
        logging.info("Error")

