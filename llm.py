from config import GENERAL_CONFIG
from google import genai
from google.genai import types


class GeminiApi:
	def __init__(self):
		self.client = genai.Client(api_key=GENERAL_CONFIG.GEMINI_API_KEY)


	def generate_completion(self, prompt: str, model: str):
		generate_content_config = types.GenerateContentConfig(
			response_mime_type = "text/json"
		)

		response = self.client.models.generate_content(
			model=model,
			contents=prompt
		)

		return response.text

if __name__ == "__main__":
	gemini_api = GeminiApi()
	completion = gemini_api.generate_completion("halo apa kabar", model=GENERAL_CONFIG.LLM_MODEL)
	print(completion)
