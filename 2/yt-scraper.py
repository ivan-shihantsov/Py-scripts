#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup
import requests
import subprocess

channel_url = "https://www.youtube.com/@MrBeast"


def get_video_ids(channel_url):
    command = ["yt-dlp", "--flat-playlist", "--print", "id", channel_url]

    result = subprocess.run(
        command, capture_output=True, text=True, check=True
    )

    video_ids = result.stdout.strip().split("\n")
    return video_ids

video_ids = get_video_ids(channel_url)


for vid in video_ids:
    link = f"https://www.youtube.com/watch?v={vid}"

    soup = BeautifulSoup(requests.get(link).content, 'lxml')
    pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
    description = pattern.findall(str(soup))[0].replace('\\n','\n')
    # print(description)

