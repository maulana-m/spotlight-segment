from spotlight.core.downloader import Downloader
from spotlight.core.service import SpotlightService
from spotlight.core.llm import GeminiApi
from spotlight.core.dto import SpotlightRequest
from spotlight.core.exceptions import VideoUrlInvalidError
import asyncio
import gradio as gr
import json

CSS = """
.spotlight-container-internal {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px; /* Adds space between items */
    padding: 20px 0; /* Adds some padding above and below the group of items */
}

.spotlight-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid #ddd;
    padding: 15px;
    margin-bottom: 25px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 350px;
    text-align: center;
}

.spotlight-topic {
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 10px;
    color: #28598a;
    word-wrap: break-word;
}

.spotlight-video {
    margin-bottom: 5px;
}
"""

spotlight_service = SpotlightService(
    _downloader=Downloader(),
    llm=GeminiApi()
)

async def run_splotlight(video_url, lang):
    try:
        request = SpotlightRequest(
          video_url=video_url,
          lang=lang
        )
    except VideoUrlInvalidError as e:
        raise gr.Error("Video Url is invalid")
    spotlights = await spotlight_service.run(request)


    html_output = """<div class="spotlight-container-internal">"""
    for row in spotlights:
        html_content = f"""
        <div class="spotlight-item">
            <div class="spotlight-topic">{row["topic_name"]}</div>
            <div class="spotlight-video">
                <iframe width="320" height="180" src="{row["embed_url"]}" frameborder="0" allowfullscreen></iframe>
            </div>
        </div>
        """
        html_output += html_content

    html_output += "</div>"

    return html_output



with gr.Blocks(css=CSS) as demo:
    gr.Markdown("## Spotlight Segment")
    video_url = gr.Textbox(label="Enter youtube url")
    lang = gr.Textbox(label="Language")
    run_button = gr.Button("Run", variant="primary")
    output_html = gr.HTML(label="Output")

    run_button.click(run_splotlight, [video_url, lang], [output_html])

    demo.queue(max_size=10).launch()
