from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from spotlight.core.exceptions import SubtitleNotFoundError
from spotlight.core.config import GENERAL_CONFIG
from spotlight.core.dto import VideoInfo
from typing import Dict, Any
import json
import requests
import logging


logger = logging.getLogger(__name__)


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
            logger.warning("Download subtitle failed")
            return None

    def get_subtitle_video(self, video_url: str) -> VideoInfo:
        video_info = self.get_video_info(video_url)
        # self.save_info(video_info, "video_info.json")
        automatic_captions = video_info.get("automatic_captions", {})

        # set english as default caption
        # TODO customize based on input languange
        origin_captions = automatic_captions.get(GENERAL_CONFIG.DEFAULT_LANGUAGE)
        if origin_captions is None:
            raise SubtitleNotFoundError("Subtitle not found")

        subtitle_url = None
        for subtitle_format in origin_captions:
            if subtitle_format.get("ext") == "ttml":
                subtitle_url = subtitle_format.get("url")

        if subtitle_url:
            subtitle_content = self.get_subtitle_content(subtitle_url)
        else:
            subtitle_content = None

        return VideoInfo(video_id=video_info.get("id"), subtitle=subtitle_content)
