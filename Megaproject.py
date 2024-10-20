import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text) 
    engine.runAndWait() 

def process_command(command):
    """Process the command and open corresponding websites."""
    command = command.lower() 
    if "open google" in command:
        webbrowser.open("https://google.com/")
        speak("Opening Google")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com") 
        speak("Opening Facebook") 
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
        speak("Opening YouTube")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn") 
    elif "open whatsapp" in command: 
        webbrowser.open("https://whatsapp.com")
        speak("Opening WhatsApp") 
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram")
    elif "open twitter" in command:
        webbrowser.open("https://twitter.com")
        speak("Opening Twitter")
    elif "open calculator" in command:
        webbrowser.open("https://calculator.com")
        speak("Opening Calculator")
    elif "open weather" in command:
        webbrowser.open("https://weather.com")
        speak("Opening Weather")
    elif command.startswith("play"):
        song = command.split(" ")[1]
        if song in musicLibrary.music: 
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry, I could not find that song.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        print("Say 'Jarvis' to activate...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration= 0.2)
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Adjusted timeouts
                word = recognizer.recognize_google(audio)
                print(f"Heard: {word}")

            if "jarvis" in word.lower():
                speak("Yes?")
                with sr.Microphone() as source: 
                    print("Jarvis Activated... Please give your command.")
                    audio = recognizer.listen(source, timeout= 5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print(f"Command received: {command}")
                    process_command(command)

        except sr.UnknownValueError:
            print("Jarvis could not understand the audio.")
            
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        
        except sr.WaitTimeoutError:
            print("Listening timed out, please try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

            
 




               #MEGA PROJECT 1: JARVIS - VOICE-ACTIVATED VIRTUAL ASSISTANT
            

""" Jarvis is a voice-activated virtual assistant designed to perform tasks such as web 
browsing, playing music, fetching news, and responding to user queries using OpenAI's 
GPT-3.5-turbo model.


FEATURES
• Voice Recognition
• Utilizes the speech_recognition library to listen for and recognize voice commands.
• Activates upon detecting the wake word "Jarvis."
• Text-to-Speech
• Converts text to speech using pyttsx3 for local conversion.
• Uses gTTS (Google Text-to-Speech) and pygame for playback.
• Web Browsing.
• Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice 


commands.


• Music Playback
• Interfaces with a musicLibrary module to play songs via web links.
• News Fetching
• Fetches and reads the latest news headlines using NewsAPI.
• OpenAI Integration
• Handles complex queries and generates responses using OpenAI's GPT-3.5-turbo.
• Acts as a general virtual assistant similar to Alexa or Google Assistant.
• Activates upon detecting the wake word "Jarvis."
• Text-to-Speech


WORKFLOW
1. Initialization
2. Greets the user with "Initializing Jarvis...."
3. Wake Word Detection
4. Listens for the wake word "Jarvis."
5. Acknowledges activation by saying "Ya."
6. Command Processing.
7. Processes commands to determine actions such as opening a website, playing 
music, fetching news, or generating a response via OpenAI.
8. Speech Output.
9. Provides responses using speak function with either pyttsx3 or gTTS.
10. Greets the user with "Initializing Jarvis...."
11. Wake Word Detection
12. Acknowledges activation by saying "Ya."
58
13. Processes commands to determine actions such as opening a website, pla """