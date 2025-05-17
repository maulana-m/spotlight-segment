from spotlight.core.downloader import Downloader
from spotlight.core.service import SpotlightService
from spotlight.core.llm import GeminiApi
from spotlight.core.dto import SpotlightRequest
import click
import asyncio


spotlight_service = SpotlightService(
    _downloader=Downloader(),
    llm=GeminiApi()
)


@click.command()
@click.option("--video_url", help="video youtube link")
@click.option("--lang", help="language output")
def run(video_url, lang):

    """Spotlight segment: Cli program to extract important segments for any youtube video"""

    async def main(video_url, lang):
        request = SpotlightRequest(
          video_url=video_url,
          lang=lang
        )
        output = await spotlight_service.run(request)
        print(output)

    if video_url is None and lang is None:
        click.echo(click.get_current_context().get_help())
    else:
        asyncio.run(main(video_url, lang))


if __name__ == '__main__':
    run()
