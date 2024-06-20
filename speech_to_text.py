import speech_recognition as sr
import text_to_speech

r = sr.Recognizer()

def listen_for_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        text_to_speech.text_to_speech("Please wake me up to interact with me")
        print("Please wake me up to interact with me")
        while True:
            audio = recognizer.listen(source,phrase_time_limit=5)
            try:
                command = recognizer.recognize_google(audio).lower()
                if "hello smart desk" in command:
                    text_to_speech.text_to_speech("thanks for waking me up how can i help you")
                    break
                else:
                    print("Oops! You have pronounced my name wrong. Try again.")
                    text_to_speech.text_to_speech("Oops! You have pronounced my name wrong. Try again.")
            except sr.UnknownValueError:
                print("Oops! You have pronounced my name wrong. Try again.")
                text_to_speech.text_to_speech("Oops! You have pronounced my name wrong. Try again.")
            except sr.RequestError:
                print("Sorry, the service is down. Try again later.")
                text_to_speech.text_to_speech("Sorry, the service is down. Try again later.")
                return

def speech_to_text():
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source,phrase_time_limit=5)
        try:
            voice_data = ""
            voice_data = r.recognize_google(audio,language="en-is")
            return voice_data
        except sr.UnknownValueError:
            print("please speak out")
        except sr.RequestError:
            print("don't be quite")


