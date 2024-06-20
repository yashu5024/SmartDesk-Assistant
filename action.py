import text_to_speech
import speech_to_text
import datetime
import webbrowser
import google

def action(data):  #data came from the speech to text
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is virtual assistant")
        return "my name is virtual assistant"

    elif "hello" in user_data or "hi" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hello, sir how are you today")
        return "hello, sir how are you today"

    elif "good morning" in user_data or " i am good" in user_data:
        text_to_speech.text_to_speech("good morning sir how can i help you")
        return "good morning sir how can i help you"

    elif "what is the time now" in user_data or "time now" in user_data:
        current_time = datetime.datetime.now()
        time = (str)(current_time.hour) + "hour" + (str)(current_time.minute) + "minutes"
        text_to_speech.text_to_speech(time)
        return time

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is opening for you")
        return "gaana.com is opening for you"

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is opening for you")
        return "youtube.com is opening for you"

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is opening for you")
        return "google.com is opening for you"

    else:
        text_to_speech.text_to_speech(google.get_answer_from_google(user_data))
        return google.get_answer_from_google(user_data)