# 🎙️ CodeClause Internship – Basic Speech Recognition Assistant (Jarvis)

A beginner-friendly Python voice assistant project built as part of the CodeClause Internship. This assistant listens for a wake word ("Jarvis") and executes system-level commands like opening apps, checking time or battery, searching Google, and more — all via your voice.

---

## 🚀 Features

- 🧠 **Custom Wake Word Activation** – Say "Jarvis" to trigger listening
- 🗣️ **Voice Commands Supported**:
  - "Hello"
  - "Open Notepad"
  - "Open File Explorer"
  - "Open Browser"
  - "Open YouTube"
  - "Open Email"
  - "Search for [query]"
  - "What time is it?"
  - "Battery percentage"
  - "Lock the screen"
  - "Goodbye" / "Exit" to close the assistant

---

## ⚙️ Tech Stack Used

- **Python 3.11**
- `speech_recognition` – Converts speech to text
- `pyttsx3` – Converts text to speech (TTS)
- `psutil` – Fetches battery status
- `webbrowser` – Opens URLs in browser
- `os`, `datetime`, `ctypes` – Perform system-level operations

---

## 📁 Project Structure

CodeClauseInternship_Basic_Speech_Recognition/
│
├── voice_assistant.py # Main Python script
├── requirements.txt # All dependencies
├── README.md # This file

---

## 🛠️ How to Run This Project

1. **Clone the repository**

```bash
git clone https://github.com/This-is-sid/CodeClauseInternship_Basic_Speech_Recognition.git
cd CodeClauseInternship_Basic_Speech_Recognition
```
2. **Install dependencies**
```bash
   pip install --upgrade pip
   pip install -r requirements.txt
```
3. **Run the assistant**
```bash
   python voice_assistant.py
```
---

#**Example Usage:**

You: Jarvis  
Assistant: Yes, I'm listening...

You: Open YouTube  
Assistant: Opening YouTube.

You: What time is it?  
Assistant: The time is 15:47.


