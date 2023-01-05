from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import random
from os.path import exists

def downloadVideo(download_link):
    cookies = {
    '__cflb': '02DiuEcwseaiqqyPC5reXswsgyrfhBQenBx2ygRTfx7aT',
    '_ga': 'GA1.2.531089767.1671927899',
    '_gid': 'GA1.2.481062388.1671927899',
    '_gat_UA-3524196-6': '1',
    }

    headers = {
    'authority': 'ssstik.io',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,ja;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__cflb=02DiuEcwseaiqqyPC5reXswsgyrfhBQenBx2ygRTfx7aT; _ga=GA1.2.531089767.1671927899; _gid=GA1.2.481062388.1671927899; _gat_UA-3524196-6=1',
    'hx-current-url': 'https://ssstik.io/en',
    'hx-request': 'true',
    'hx-target': 'target',
    'hx-trigger': '_gcaptcha_pt',
    'origin': 'https://ssstik.io',
    'referer': 'https://ssstik.io/en',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': download_link,
        'locale': 'en',
        'tt': 'NDZuMTU2',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    download = BeautifulSoup(response.text, "html.parser")

    download_link = download.a["href"]

    mp4File = urlopen(download_link)
    with open(f"tiktok_videos/video_{random_number_tiktok1}_{random_number_tiktok2}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break
random_number_tiktok1 = random.randint(1, 9999999)
random_number_tiktok2 = random.randint(1, 9999999)

""" def downloadImage(linkI):
    cookies = {
        '__cflb': '02DiuEcwseaiqqyPC5reXswsgyrfhBQenBx2ygRTfx7aT',
        '_ga': 'GA1.2.531089767.1671927899',
        '_gid': 'GA1.2.372182661.1672415510',
        '_gat_UA-3524196-6': '1',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,ja;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cflb=02DiuEcwseaiqqyPC5reXswsgyrfhBQenBx2ygRTfx7aT; _ga=GA1.2.531089767.1671927899; _gid=GA1.2.372182661.1672415510; _gat_UA-3524196-6=1',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': linkI,
        'locale': 'en',
        'tt': 'QmtTTGIz',
    }

    responseI = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadI = BeautifulSoup(responseI.text, "html.parser")
    download_linkI = downloadI.a["href"]

    image = urlopen(download_linkI)
    with open(f"tiktok_videos/photo_{random_image_tiktok1}_{random_image_tiktok2}.png", "wb") as output:
        while True:
            data = image.read(4096)
            if data:
                output.write(data)
            else:
                break
random_image_tiktok1 = random.randint(1, 9999999)
random_image_tiktok2 = random.randint(1, 9999999) """
