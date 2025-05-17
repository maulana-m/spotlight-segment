from spotlight.core.config import GENERAL_CONFIG
from google import genai
from google.genai import types


class GeminiApi:
    def __init__(self):
        self.client = genai.Client(api_key=GENERAL_CONFIG.GEMINI_API_KEY)

    async def generate_completion(self, prompt: str, model: str, response_mime_type: str, response_schema=None):
        config = types.GenerateContentConfig(
            response_mime_type=response_mime_type,
            response_schema=response_schema
        )

        response = await self.client.aio.models.generate_content(
            model=model,
            contents=prompt,
            config=config
        )

        return response
