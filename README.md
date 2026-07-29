# Nayra - Offline AI Voice Assistant

Nayra is a lightweight offline AI voice assistant built with Python that combines speech recognition, natural text-to-speech, and a local Ollama language model. It can understand voice commands, play music on YouTube, tell the time and date, answer predefined questions, and generate intelligent conversational responses without relying on cloud-based AI services.

## Features

* Voice command recognition using SpeechRecognition
* Natural English (India) text-to-speech using Edge TTS
* Offline AI responses through a local Ollama model
* Play songs directly on YouTube
* Tell the current time and date
* Answer predefined personal assistant commands
* Lightweight and easy to extend with new commands
* Simple Python codebase suitable for beginners and CSE projects

## Tech Stack

* Python 3
* SpeechRecognition
* Edge TTS
* Pygame
* Requests
* PyWhatKit
* Ollama (local LLM)

## Project Structure

```
nayra/
├── main.py          # Entry point
├── function.py      # Voice assistant logic
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/nayra.git
cd nayra
```

2. Create a virtual environment (optional)

```bash
python -m venv .venv
```

3. Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

## Ollama Setup

Install Ollama from https://ollama.com and download a lightweight model.

```bash
ollama pull phi
```

Make sure the Ollama server is running.

```bash
ollama serve
```

## Run

```bash
python main.py
```

Nayra will greet you and start listening for voice commands.

## Example Commands

* "Play Believer"
* "What is the time?"
* "What is the date today?"
* "Who is your creator?"
* "What is your name?"

Any other command is forwarded to the local Ollama model for a conversational response.

## Requirements

* Python 3.10+
* Microphone
* Internet connection for speech recognition and YouTube playback
* Ollama installed locally for AI responses

## Future Improvements

* Hindi and multilingual support
* Application control (open/close software)
* File and folder management
* Email and messaging automation
* Wake-word detection
* Background system service mode
* Smart home and IoT integration

## Author

Developed by **Aryan Mishra** as a lightweight offline AI voice assistant project for learning, experimentation, and future expansion into a full desktop automation assistant.
