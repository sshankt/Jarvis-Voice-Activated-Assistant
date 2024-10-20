# 🤖 JARVIS - Voice-Activated Virtual Assistant

**Jarvis** is a voice-activated virtual assistant designed to perform tasks such as 
web browsing, playing music, open app etc. It functions similarly to other virtual assistants like Alexa and Google Assistant but with customizable features.

---

## 🌟 Key Features

| Feature               | Description                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| 🎙️ **Voice Recognition**   | Utilizes the `speech_recognition` library to listen for and recognize voice commands.          |
| 🗣️ **Text-to-Speech**      | Converts text to speech using `pyttsx3` for local TTS, and `gTTS` (Google Text-to-Speech) with `pygame` for playback. |
| 🌐 **Web Browsing**        | Opens websites such as Google, Facebook, YouTube, and LinkedIn based on voice commands.   |
| 🎶 **Music Playback**      | Plays music from web links via the `musicLibrary` module.                                  |
|                                         |

---

## 🛠️ How Jarvis Works

1. **Initialization**: 
   - Greets the user with **"Initializing Jarvis..."**.
   
2. **Wake Word Detection**:
   - Listens for the wake word **"Jarvis"** and acknowledges activation with **"Ya"**.

3. **Command Processing**:
   - Processes the command to determine actions, such as:
     - Opening a website 🌐
     - Playing music 🎶
    - open app
4. **Speech Output**:
   - Provides responses using either the `pyttsx3` library for local TTS or `gTTS` for online TTS, with playback managed by `pygame`.

---

## 🖥️ Project Workflow

1. **Startup**: 
   - Jarvis initializes and greets the user with **"Initializing Jarvis..."**.

2. **Voice Activation**: 
   - Listens for the wake word **"Jarvis"**.

3. **Command Execution**: 
   - Executes tasks such as opening websites, playing music, or fetching news based on user commands.

4. **Response Delivery**: 
   - Delivers results through speech using TTS methods (`pyttsx3` or `gTTS`).



## 📚 Libraries Used
speech_recognition: For detecting voice input.
pyttsx3: For offline text-to-speech conversion.
webbrowser : for opening app
musiclibary : for music 
