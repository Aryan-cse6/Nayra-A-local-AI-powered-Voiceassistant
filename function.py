import datetime
import speech_recognition as sr
import pywhatkit
import requests
import edge_tts
import asyncio
import pygame
import io
listener = sr.Recognizer()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)

        print("Recognizing...")
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)

    except Exception as e:
        print("Error:", e)

    return command

pygame.mixer.init()
async def speak(text):
    communicate = edge_tts.Communicate(text, "en-IN-NeerjaNeural", rate="+25%"  )
    stream = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            stream += chunk["data"]
    return stream

def talk(text):
    try:
        audio_data = asyncio.run(speak(text))
        audio_file = io.BytesIO(audio_data)
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(20)   # prevents 100% CPU usage

    except Exception as e:
        print("Speech error:", e)

def ask_ai_local(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",   # Use smaller model for speed (run: ollama pull phi)
                "prompt": f"""
You are NAAYRA.
A calm, intelligent, composed female AI.
User: {prompt}
NAYRA:
""",
                "temperature": 0.5,
                "max_tokens": 40,
                "stream": False,
                "options": {
            "num_ctx": 1024,
            "num_thread": 4
        }

            }
        )

        result = response.json()
        return result.get("response", "I couldn't process that properly.")

    except Exception as e:
        print("Local AI Error:", e)
        return "My local brain is not responding."
def run_nayra():
 while True:
  command = take_command()
  if command == "":
         continue
  if "play" in command:
         song= command.replace("play","")
         talk("playing"+song)
         pywhatkit.playonyt(song)
  elif 'time' in command:
         time=datetime.datetime.now().strftime('%I : %M %p')
         print(time)
         talk('Current time is'+time)
  elif 'who is your creator' in command:
       talk('Aaryan Mishra is my creator.')
  elif 'date' in command:
          current_date = datetime.date.today()
          current_day = datetime.datetime.today().strftime('%A')
          print(current_date, current_day)
          talk('today is'+str(current_date)+'And the day is'+ current_day)
  elif 'what is your name' in command:
     talk('My name is naayra')
  elif 'how old you are'in command:
      talk('i am 1 month old')
  elif 'whats your age'in command:
      talk('i am 1 month old')
  else:
    reply = ask_ai_local(command)
    print(reply)
    talk(reply)

