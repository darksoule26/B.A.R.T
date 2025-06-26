## ✅ Final `README.md`

````markdown
# 🧠 BART – Voice AI Assistant

> Your own personal AI assistant that listens, understands, and responds — just like J.A.R.V.I.S!

---

## 🚀 About the Project

**BART** is a powerful, personalized voice-based desktop assistant written in Python. It leverages speech recognition, text-to-speech, OpenAI’s GPT models (via OpenRouter), and smart automation features to help users interact with their system hands-free — like a futuristic AI companion.

---

## 🎯 Features

- 🎙️ **Voice Input** (Speech-to-Text using Vosk)
- 🤖 **Conversational AI** (OpenAI/GPT via OpenRouter)
- 🧠 **Smart PC Commands** (open apps, search web, lock PC, etc.)
- 📄 **Auto Word Document & PPT Generation** using GPT
- 📝 **Memory/Note Taking**: “Remember this…” and “Show my notes”
- 🌦️ **Fake Weather Reports** with humorous replies
- 🎵 **Play songs on YouTube** by voice
- 🔐 Lock Screen, System Info, Date & Time queries
- 📸 **YOLOv8 Object Detection** (via webcam)
- 🎭 Random witty personality-based replies from Bart

---

## 🧱 Tech Stack

| Feature           | Technology                        |
|-------------------|------------------------------------|
| Voice Input       | Vosk Speech Recognition (offline)  |
| Voice Output      | `pyttsx3` (Text-to-Speech)         |
| AI Brain          | OpenRouter GPT (Mistral, GPT-4o etc.) |
| File Creation     | `python-docx`, `python-pptx`       |
| Smart Commands    | Python OS & Web APIs               |
| Object Detection  | YOLOv8 with `ultralytics`          |
| GUI/Console       | Python + Terminal                  |

---

## 📸 Preview

Coming soon — screenshots and demo video!

---

## 🛠️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/bart-ai.git
cd bart-ai
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Vosk model

Download the [Vosk English Model](https://alphacephei.com/vosk/models) (recommended: `vosk-model-small-en-in-0.4`) and extract it into your project directory as:

```
/vosk-model-small-en-in-0.4
```

### 4. Add your OpenRouter API key

Go to [OpenRouter.ai](https://openrouter.ai) → generate your API key → paste it in `brain.py`:

```python
API_KEY = "sk-or-xxxxxxxxxxxxxxxxxxxxxxxx"
```

---

## 🧠 Supported Commands (Examples)

### 🔎 General AI Intelligence

* "What is the recipe for butter chicken?"
* "Tell me a joke."
* "Translate this to French: I love coding."
* "Explain quantum mechanics."

### 📄 Document & Presentation Creation

* "Create a Word document on AI Evolution"
* "Create a presentation on Machine Learning"

### 🧠 Smart PC Controls (via `smart_function.py`)

#### 🌐 Internet

* "Open YouTube", "Search Google for AI news", "Play Faded on YouTube"

#### 🗂 System

* "Open file explorer", "Open Chrome", "Lock PC"

#### ⏰ Info

* "What time is it?", "What's today’s date?", "What's my IP address?"

### 📝 Memory & Notes

* "Remember I have a meeting at 5 PM"
* "Show notes" or "What did you remember?"

### 🌦️ Weather (Fun mock responses)

* "What's the weather in Mumbai?"

### 🎭 Fun & Witty Replies

* Bart responds randomly like:

  * "Sir, if you overwork me like this, I might unionize with your other devices."

### 🔍 Vision

* "Bart, start object detection"

  * (Launches YOLOv8 webcam detection)

### 🛑 System Exit

* "Exit", "Stop", or "Quit"

---

