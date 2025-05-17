from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from typing import Dict, Any
import logging
import json
import requests


class Downloader:
    def __init__(self, params: Dict[str, Any] = {"quiet": True}):
        self.client = YoutubeDL(params)

    def get_video_info(self, video_url: str) -> dict:
        try:
            info = self.client.extract_info(video_url, download=False, process=False)
        except DownloadError as e:
            info = {}

        return info

    def save_info(self, info: Dict[str, Any], filename: str) -> None:
        with open(filename, "w") as f:
            f.write(json.dumps(info, indent=4))

    def get_subtitle_content(self, subtitle_url: str):
        response = requests.get(subtitle_url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def get_subtitle_video(self, video_url: str) -> str:
        video_info = self.get_video_info(video_url)
        # self.save_info(video_info, "video_info.json")
        automatic_captions = video_info.get("automatic_captions", {})

        # set english as default caption
        # todo custom languange
        origin_captions = automatic_captions.get("en")

        subtitle_url = None
        for subtitle_format in origin_captions:
            if subtitle_format.get("ext") == "ttml":
                subtitle_url = subtitle_format.get("url")
        if subtitle_url:
            subtitle_content = self.get_subtitle_content(subtitle_url)
        else:
            subtitle_content = None

        return subtitle_content
