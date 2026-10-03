import os
import json
# pyrefly: ignore [missing-import]
from flask import Flask, request, jsonify, send_from_directory
from agent import generate_meeting_notes, format_notes

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    transcript = (data or {}).get("transcript", "").strip()
    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400
    try:
        notes = generate_meeting_notes(transcript)
        markdown = format_notes(notes)
        return jsonify({"notes": notes, "markdown": markdown})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
