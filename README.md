# MeetNote

MeetNote is an AI-powered meeting note-taking application. It takes a raw meeting transcript and uses Google's Gemini AI to automatically generate structured meeting notes, including:
- Executive Summary
- Participants and Duration
- Key Decisions
- Action Items (with owners and due dates)
- Blockers
- Next Meeting details

## Features
- **Clean Web Interface**: A modern, dark-themed Flask frontend to easily paste transcripts or upload `.txt` files.
- **Structured Output**: Generates clean, readable Markdown that you can download directly from the browser.
- **Robust AI Backend**: Uses `langchain-google-genai` and `gemini-3.8-flash` with built-in retry logic and exponential backoff to handle API rate limits gracefully.

## Project Structure
- `agent.py`: The core LLM logic for parsing transcripts and formatting notes.
- `app.py`: The Flask web server providing the API and serving the frontend.
- `static/index.html`: The lightweight HTML/CSS/JS frontend.
- `requirements.txt`: Python dependencies.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**:
   Create a `.env` file in the root directory and add your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   *You can get a free key from [Google AI Studio](https://aistudio.google.com/apikey).*

## Usage

Start the web server:
```bash
python app.py
```
Then open `http://localhost:5000` in your web browser. Paste your transcript or upload a file, and click "Generate Notes".

Alternatively, you can run the agent directly from the command line:
```bash
python agent.py --transcript your_transcript.txt
```
