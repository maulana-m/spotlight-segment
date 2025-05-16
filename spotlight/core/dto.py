from pydantic import BaseModel, Field


class SpotlightSchema(BaseModel):
    topic_name: str
    start_time: str
    end_time: str


class SpotlightRequest(BaseModel):
    video_url: str
    lang: str
