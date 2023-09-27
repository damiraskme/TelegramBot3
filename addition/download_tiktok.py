from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import os
import logging

def downloadVideo(download_link, id):
    cookies = {
        '_gid': 'GA1.2.1702673078.1693846189',
        '__cflb': '0H28v8EEysMCvTTqtu4kewtscz2STFoqACKREdxQzZ3',
        '_gat_UA-3524196-6': '1',
        '_ga': 'GA1.2.590353548.1693846189',
        '_ga_ZSF3D6YSLC': 'GS1.1.1693929051.3.1.1693929188.0.0.0',
    }
    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,ja;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gid=GA1.2.1702673078.1693846189; __cflb=0H28v8EEysMCvTTqtu4kewtscz2STFoqACKREdxQzZ3; _gat_UA-3524196-6=1; _ga=GA1.2.590353548.1693846189; _ga_ZSF3D6YSLC=GS1.1.1693929051.3.1.1693929188.0.0.0',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    params = {
        'url': 'dl',
    }
    data = {
        'id': f'{download_link}',
        'locale': 'en',
        'tt': 'Y0h6Q1Bk',
    }
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    download = BeautifulSoup(response.text, "html.parser")
    download_link = download.a["href"]
    mp4File = urlopen(download_link)
    with open(f"addition/videos/file_{id}.mp4", "wb") as output:
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
    
    with open(f"addition/videos/file_{id}.mp4", "wb") as file:
        file.write(response.content)
        return "File written"
    # except Exception:
    #     return "Cant write file"
    
def deleteTiktok(id: str):
    try:
        if (os.path.isfile(f"addition/videos/file_{id}.mp4")):
            os.remove(f"addition/videos/file_{id}.mp4")
            logging.info("File deleted")
    except FileNotFoundError:
        logging.info("Error")

    
