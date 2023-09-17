from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import os
import logging

def downloadVideo(download_link, id):
    cookies = {
        """
        cookies
        """
    }
    headers = {
        """
        headers
        """
    }
    params = {
        """
        params
        """
    }
    data = {
        'id': f'{download_link}',
        'locale': 'en',
        'tt': 'tt',
    }
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    download = BeautifulSoup(response.text, "html.parser")
    download_link = download.a["href"]
    mp4File = urlopen(download_link)
    with open(f"videos/file_{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break

def checkUrl(url: str) -> bool:
    if (url[8] == "v" and url[9] == "m"):
        return True
    return False

def getId(url: str) -> str:
    if (checkUrl(url)):
        response = requests.get(url)
        url = response.url
    start = url.find("video/") + 6
    end = url.find("?_")
    url = url[start:end]
    return url

def downloadTiktok(video: str, id: str):
    url = "https://tikcdn.io/ssstik/" + video
    response = requests.get(url)
    
    with open(f"videos/file_{id}.mp4", "wb") as file:
        file.write(response.content)
        return "File written"
    # except Exception:
    #     return "Cant write file"
    
def deleteTiktok(id: str):
    try:
        if (os.path.isfile(f"videos/file_{id}.mp4")):
            os.remove(f"videos/file_{id}.mp4")
            logging.info("File deleted")
    except FileNotFoundError:
        logging.info("Error")

    
