<div align="center">
  <h1>📝 MeetNote</h1>
  <p><strong>AI-Powered Meeting Intelligence & Automated Notes</strong></p>
  
  [![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-3.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
  [![Gemini](https://img.shields.io/badge/Google_Gemini-3.8_Flash-orange.svg)](https://deepmind.google/technologies/gemini/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
</div>

<br />

MeetNote is an intelligent meeting assistant that transforms raw conversational transcripts into highly structured, actionable executive summaries. Powered by Google's Gemini LLM and LangChain, it extracts key decisions, assigns action items, and flags project blockers automatically.

## ✨ Key Features

- **🧠 Intelligent Extraction**: Automatically identifies executive summaries, key decisions, action items (with owners and deadlines), and blockers.
- **🛡️ Resilient Architecture**: Built-in exponential backoff and retry logic to gracefully handle API rate limits and transient LLM unavailability.
- **💻 Modern Web Interface**: Clean, responsive, dark-themed UI built with HTML5/CSS3 (no heavy frontend frameworks required).
- **📥 Dual Input Modes**: Support for direct text pasting or `.txt` file uploads.
- **📄 Markdown Export**: Instantly download formatted meeting notes as portable `.md` files.
- **⚡ Fast & Lightweight**: Powered by Flask and `gemini-3.8-flash` for rapid inference and minimal footprint.

## 🏗️ System Architecture

```text
meetnote/
├── agent.py               # Core LLM logic, LangChain orchestration, and retry mechanisms
├── app.py                 # Flask REST API and static file server
├── static/
│   └── index.html         # Single-page frontend application
├── .env                   # Environment variables (API Keys)
└── requirements.txt       # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- A Google Gemini API Key ([Get one for free at Google AI Studio](https://aistudio.google.com/apikey))

### Installation

1. **Clone the repository** (or download the source):
   ```bash
   git clone https://github.com/yourusername/meetnote.git
   cd meetnote
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root and add your API key:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

## 💻 Usage

### Web Interface (Recommended)

Start the local Flask server:
```bash
python app.py
```
Navigate to `http://localhost:5000` in your web browser. You can paste a transcript directly or upload a `.txt` file to generate your notes.

### Command Line Interface

For batch processing or headless usage, you can run the agent directly:
```bash
python agent.py --transcript path/to/your_transcript.txt
```
The output will be printed to the console and automatically saved as a `.md` file in the current directory.

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **AI/LLM**: Google Gemini (`gemini-3.8-flash`), LangChain (`langchain-google-genai`)
- **Frontend**: Vanilla HTML5, CSS3, JavaScript

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
