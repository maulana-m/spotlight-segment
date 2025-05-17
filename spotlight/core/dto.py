from pydantic import BaseModel, field_validator, ValidationError
from spotlight.core.exceptions import VideoUrlInvalidError
import re


class SpotlightSchema(BaseModel):
    topic_name: str
    start_time: str
    end_time: str


class VideoInfo(BaseModel):
    video_id: str
    subtitle: str


class SpotlightRequest(BaseModel):
    video_url: str
    lang: str

    @field_validator("video_url")
    def is_valid_youtube_url(cls, value):
        pattern = r"^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.*[\w-]+\/?$"
        match = re.match(pattern, value)
        if not bool(match):
            raise VideoUrlInvalidError("URL must be a youtube URL")
        return value
