import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize text-to-speech engine once globally for efficiency
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    print(f"Processing command: {command}")
    command = command.lower()
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")
    else:
        speak("Sorry, I didn't understand the command.")


if __name__ == "__main__":
    speak("Initializing Jarvis")

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                # Calibrate ambient noise BEFORE listening
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening for wake word...")

                # Listen for wake word with timeout, catch timeout later
                audio = recognizer.listen(source, timeout=4)

            command = recognizer.recognize_google(audio)
            print(f"Heard: {command}")

            if command.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("Jarvis active, listening for command...")
                    audio = recognizer.listen(source, timeout=4)

                command = recognizer.recognize_google(audio)
                print(f"Command received: {command}")
                processCommand(command)

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected within 4 seconds, retrying...")

        except sr.UnknownValueError:
            print("Jarvis can't understand")

        except sr.RequestError as e:
            print(f"error {e}")
