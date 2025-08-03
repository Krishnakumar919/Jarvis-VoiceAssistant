# Jarvis Voice Assistant

A simple desktop voice assistant built with Python that listens for a wake word ("Jarvis") and executes basic voice commands like opening websites. This project demonstrates speech recognition, text-to-speech, and command parsing using Python libraries.

---

## Features

- Wake-word activated voice assistant using the microphone.
- Uses `SpeechRecognition` (Google API) for speech-to-text.
- Uses `pyttsx3` for text-to-speech replies.
- Supports simple web automation commands, such as opening Google or Facebook.
- Modular and easy to extend with new voice commands.

---

## Limitations

- Limited set of voice commands currently implemented.
- Recognition accuracy depends on the quality of microphone and ambient noise.
- Requires internet connection for Google speech recognition.
- The assistant only works when the wake word "Jarvis" is spoken.
- No natural language processing or complex contextual understanding yet.

---

## Requirements

- **Python 3.7+**  
- Libraries:  
  - `SpeechRecognition`  
  - `pyttsx3`  
  - `pyaudio` or `PyAudio` (for microphone input)  
  - `webbrowser` (built-in Python module)  

> Note: `pyaudio` can be tricky to install on some platforms; binary wheels or platform-specific methods may be needed.

---

## Setup Instructions

1. **Clone or download the repository**

git clone https://github.com/Krishnakumar919/Jarvis-VoiceAssistant.git
cd Jarvis-VoiceAssistant

text

2. **Create and activate a virtual environment** (recommended)

On Windows PowerShell:

python -m venv venv
.\venv\Scripts\activate

text

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

text

3. **Install required libraries**

pip install SpeechRecognition pyttsx3 pyaudio

text

If `pyaudio` installation fails:
- On Windows, consider downloading a pre-built wheel from [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
- On macOS/Linux, ensure you have PortAudio installed (`brew install portaudio` or use your package manager) before installing `pyaudio`.

4. **Run the assistant**

python main.py

text

The assistant will speak an initialization message and listen for the wake word "Jarvis".

---

## How to Use

- Say **"Jarvis"** clearly to activate the assistant.
- After activation, issue a command such as:
- "Open Google"
- "Open Facebook"

- The assistant will open the corresponding website in your default browser.

---

## Extending the Assistant

This assistant is built with modular code, making it easy to add new functionalities:

- Add new commands by editing the `processCommand()` function in `main.py`.
- Each command can be matched using keywords in the recognized text.
- Additional features like playing music, checking weather, or telling jokes can be added by creating dedicated functions and integrating into the command processing.

Example:

def processCommand(command):
if "open youtube" in command.lower():
speak("Opening YouTube")
webbrowser.open("https://www.youtube.com/")
# Add more commands here

text

Feel free to fork the repo and create your own extensions!

---

## Troubleshooting

- **Microphone not found or not working**: Ensure your microphone is set as the default recording device and is not muted.
- **`WaitTimeoutError` or recognition errors**: Speak clearly and promptly after the "Listening" prompt. Adjust or remove timeout parameters in `main.py` if needed.
- **`pyaudio` installation issues**: Refer to the platform-specific notes for installing PortAudio and PyAudio.

---

## License

This project is provided as-is for educational purposes. Feel free to modify and use it under the MIT License.

---

## Contact

Created by Krishna Kumar  
GitHub: [https://github.com/Krishnakumar919](https://github.com/Krishnakumar919)  
Email: krishnakeshav.kk919@gmail.com

---

Happy coding! 🚀
