from pydantic_settings import BaseSettings


class GeneralConfig(BaseSettings):
	GEMINI_API_KEY: str = ""
	LLM_MODEL: str = "gemini-2.0-flash"

	class Config:
		env_prefix = "GENERAL_CONFIG_"


GENERAL_CONFIG = GeneralConfig()
