
# Spotlight segment

Spotlight Segment is an application that automatically identifies and extracts 'spotlight segments' from YouTube videos, providing you with a timeline of key moments. It leverages the power of Large Language Model (LLM) to understand video content and pinpoint the most relevant sections.


## Getting Started

### 1. Use uv for project management 

See https://docs.astral.sh/uv/ for installation


### 2. Install packages dependency

```bash
uv sync
```

### 3. Run the localhost server
```bash
make run
```
This will start the FastAPI server using uvicorn on `http://localhost:5000`.

### 4. Test the API Endpoint

You can test the streaming endpoint using `curl`  or any API software like postman.

#### Example using `curl`:
```bash
curl --location 'localhost:5000/segments' \
--header 'Content-Type: application/json' \
--data  '{
"video_url": "https://www.youtube.com/watch?v=P2Ulfv9xaFk",
"lang": "en"
}'
```

