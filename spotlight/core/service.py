from spotlight.core.downloader import Downloader
from spotlight.core.llm import GeminiApi
from spotlight.core.dto import SpotlightRequest, SpotlightSchema
from spotlight.core.constant import PROMPT_TEMPLATE
from spotlight.core.config import GENERAL_CONFIG


class SpotlightService:
    def __init__(self, _downloader, llm):
        self.downloader = _downloader
        self.llm = llm

    async def run(self, splotlight_request):
        video_url = splotlight_request.video_url
        lang = splotlight_request.lang

        subtitle = self.downloader.get_subtitle_video(video_url)
        prompt = self.construct_prompt(lang, subtitle)
        # print(prompt)
        response_schema = list[SpotlightSchema]

        response_llm = await self.llm.generate_completion(
            prompt=prompt,
            model=GENERAL_CONFIG.LLM_MODEL,
            response_mime_type="application/json",
            response_schema=response_schema
        )
        response = self._parse_completion(response_llm)

        return response

    def construct_prompt(self, language: str, xml_subtitle: str):
        prompt = (PROMPT_TEMPLATE
            .replace("{{language}}", language)
            .replace("{{xml_subtitle}}", xml_subtitle)
        )

        return prompt

    def _parse_completion(self, response_llm):
        response = [x.model_dump() for x in response_llm.parsed]

        return response
