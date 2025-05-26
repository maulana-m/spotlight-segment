from spotlight.core.downloader import Downloader
from spotlight.core.service import SpotlightService
from spotlight.core.llm import GeminiApi
from spotlight.core.dto import SpotlightRequest
from spotlight.core.exceptions import VideoUrlInvalidError
import asyncio
import gradio as gr
import json

CSS = """
.spotlight-item {
    display: flex;
    flex-direction: column; /* Stack topic name above the video */
    align-items: center; /* Center the content horizontally */
    border: 1px solid #ddd;
    padding: 15px; /* Increased padding */
    margin-bottom: 25px; /* Increased margin for spacing */
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: 350px; /* Set a fixed width for consistency */
    text-align: center; /* Center the text in the topic name */
}

.spotlight-topic {
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 10px; /* Increased margin */
    color: #28598a; /* A nicer color */
    word-wrap: break-word; /* Handle long topic names */
}

.spotlight-video {
    /* Add some margin around the iframe, if needed */
    margin-bottom: 5px;
}

/* Optional: If you want the spotlight items to display in a row */
.gradio-container {
    display: flex; /* Use flexbox to arrange items in a row */
    flex-wrap: wrap; /* Allow items to wrap to the next line if they don't fit */
    justify-content: center; /* Distribute items evenly */
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


    html_output = ""
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

    return html_output



with gr.Blocks(css=CSS) as demo:
    video_url = gr.Textbox(label="Enter youtube url")
    lang = gr.Textbox(label="Language")
    run_button = gr.Button("Run", variant="primary")
    output_html = gr.HTML(label="Output")

    run_button.click(run_splotlight, [video_url, lang], [output_html])

    demo.queue(max_size=10).launch()
