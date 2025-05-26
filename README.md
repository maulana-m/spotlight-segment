
# Spotlight segment

Spotlight Segment is an application that automatically identifies and extracts 'spotlight segments' from YouTube videos, providing you with a timeline of key moments. It leverages the power of Large Language Model (LLM) to understand video content and pinpoint the most relevant sections.


## Getting Started

### 1. Use uv for project management 

See https://docs.astral.sh/uv/ for installation


### 2. Install packages dependency

```bash
uv sync
```

### 3. Run API server
```bash
make run
```
This will start the FastAPI server using uvicorn on `http://localhost:5000`.

#### Test the API Endpoint

You can test the streaming endpoint using `curl`  or any API software like postman.

#### Example using `curl`:
```bash
curl -X 'POST' \
  'http://localhost:5000/segments' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "video_url": "https://www.youtube.com/watch?v=P2Ulfv9xaFk",
  "lang": "en"
}'
```

Output response
```json
{
    "data": [
        {
            "topic_name": "Liverpool's Missed Chances and Arsenal's Defensive Block",
            "start_time": "00:00:04.160",
            "end_time": "00:00:10.679",
            "embed_url": "https://youtube.com/embed/P2Ulfv9xaFk?&start=4&end=10&autoplay=1"
        },
        {
            "topic_name": "Liverpool Takes the Lead: Gakpo Scores After Missed Chance",
            "start_time": "00:00:39.040",
            "end_time": "00:00:47.600",
            "embed_url": "https://youtube.com/embed/P2Ulfv9xaFk?&start=39&end=47&autoplay=1"
        },
        {
            "topic_name": "Diaz Extends Liverpool's Lead with Glorious Goal",
            "start_time": "00:00:55.199",
            "end_time": "00:01:02.239",
            "embed_url": "https://youtube.com/embed/P2Ulfv9xaFk?&start=55&end=62&autoplay=1"
        },
        {
            "topic_name": "Arsenal's Martinelli Scores: A Flicker of Hope",
            "start_time": "00:01:20.080",
            "end_time": "00:01:28.479",
            "embed_url": "https://youtube.com/embed/P2Ulfv9xaFk?&start=80&end=88&autoplay=1"
        },
        {
            "topic_name": "Mourinho's Tackle Leads to Second Yellow Card",
            "start_time": "00:01:38.439",
            "end_time": "00:01:54.479",
            "embed_url": "https://youtube.com/embed/P2Ulfv9xaFk?&start=98&end=114&autoplay=1"
        },
        {
            "topic_name": "Last Chance Corner: Controversial Goal Disallowed",
            "start_time": "00:01:52.720",
            "end_time": "00:02:08.319",
            "embed_url": "https://youtube.com/embed/P2Ulfv9xaFk?&start=112&end=128&autoplay=1"
        },
        {
            "topic_name": "Liverpool and Arsenal Draw: A Hard-Fought Battle",
            "start_time": "00:02:08.319",
            "end_time": "00:02:20.000",
            "embed_url": "https://youtube.com/embed/P2Ulfv9xaFk?&start=128&end=140&autoplay=1"
        }
    ],
    "status": "success"
}
```


### 4. Run with Gradio
```bash
make gradio
```
This will start the gradio server on `http://localhost:7860`.

Go to your browser and navigate to that dedicated link. Input any youtube url and the languange, Then click run button to running the program. 

#### Example output
![Image](https://github.com/user-attachments/assets/1fd08a9a-8a81-4837-b8d3-ae8ddbfd14f1)
