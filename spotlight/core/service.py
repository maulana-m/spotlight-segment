from spotlight.core.downloader import Downloader
from spotlight.core.llm import GeminiApi
from spotlight.core.dto import SpotlightRequest, SpotlightSchema
from spotlight.core.constant import PROMPT_TEMPLATE
from spotlight.core.config import GENERAL_CONFIG


EMBED_URL = "https://youtube.com/embed/{id}?&start={start_time}&end={end_time}&autoplay=1"


class SpotlightService:
    def __init__(self, _downloader: Downloader, llm: GeminiApi):
        self.downloader = _downloader
        self.llm = llm

    async def run(self, splotlight_request: SpotlightRequest):
        video_url = splotlight_request.video_url
        lang = splotlight_request.lang

        video_info = self.downloader.get_subtitle_video(video_url)
        prompt = self.construct_prompt(lang, video_info.subtitle)

        response_schema = list[SpotlightSchema]

        response_llm = await self.llm.generate_completion(
            prompt=prompt,
            model=GENERAL_CONFIG.LLM_MODEL,
            response_mime_type="application/json",
            response_schema=response_schema
        )
        response = self._parse_response(response_llm, video_info.video_id)

        return response

    def construct_prompt(self, language: str, xml_subtitle: str) -> str:
        prompt = (PROMPT_TEMPLATE
            .replace("{{language}}", language)
            .replace("{{xml_subtitle}}", xml_subtitle)
        )

        return prompt

    def _parse_response(self, response_llm, video_id):
        response = [x.model_dump() for x in response_llm.parsed]

        for data in response:
            data["embed_url"] = self._embed_timeline(video_id, data["start_time"], data["end_time"])

        return response

    def _embed_timeline(self, video_id: str, start_time: str, end_time: str) -> str:
        def time_to_second(time_str: str):
            hours, minutes, seconds = time_str.split(':')
            seconds = seconds[:2]
            return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

        embed_url = EMBED_URL.format(
            id=video_id,
            start_time=time_to_second(start_time),
            end_time=time_to_second(end_time)
        )

        return embed_url
