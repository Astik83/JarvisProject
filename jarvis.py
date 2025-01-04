import datetime
import random
import pyttsx3
import speech_recognition as sr
import os
import cv2
from requests import get
import wikipedia
import webbrowser
from urllib.parse import quote
import pywhatkit as kit
import pyjokes
from threading import Timer

# Contact list mapping names to phone numbers
contact_list = {
    "aastik": "+9779746637118",
    "dad": "+9779825949045",
    "archana": "+9779707665488",
    "anisha": "+9779825956070",
    "pankaj": "+9779819981054",
    "shivam": "+919263899895"
}

# Replace these with your actual API keys
weather_api_key = "83a3949fdf634904c5f586b3b5adb105"

engine = pyttsx3.init('sapi5')  # Initialize the engine using the 'sapi5' driver
voices = engine.getProperty('voices')  # Get available voices
engine.setProperty('voice', voices[0].id)  # Set the engine to use the first voice


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception:
        speak("Say that again, please...")
        return "none"
    return query.lower()



def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Astik")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon Astik")
    else:
        speak("Good Evening Astik")
    speak("I am Jarvis. Please tell me how I can help you")


def schedule_message(contact_name, message, delay_minutes):
    phone_number = contact_list.get(contact_name.lower())
    if phone_number:
        now = datetime.datetime.now()
        send_time = now + datetime.timedelta(minutes=delay_minutes)
        hour = send_time.hour
        minute = send_time.minute
        kit.sendwhatmsg(phone_number, message, hour, minute)
        speak(f"Message scheduled to be sent to {contact_name} at {hour:02}:{minute:02}.")
    else:
        speak("Contact not found.")


def handle_query(query):
    if "open notepad" in query:
        os.startfile("notepad.exe")
    elif "close notepad" in query:
        close_application("notepad.exe")
    elif "open microsoft word" in query:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    elif "close microsoft word" in query:
        close_application("WINWORD.EXE")
    elif "open command prompt" in query:
        os.startfile("cmd.exe")
    elif "close command prompt" in query:
        close_application("cmd.exe")
    elif "open camera" in query or "open the camera" in query:
        open_camera()
    elif "play movie" in query:
        play_movie()
    elif "ip address" in query or "my ip address" in query:
        get_ip_address()
    elif "wikipedia" in query:
        search_wikipedia(query)
    elif "open youtube" in query or "search on youtube" in query or "youtube search" in query:
        search_youtube()
    elif "open google" in query or "search on google" in query or "google search" in query:
        search_google()
    elif "open facebook" in query:
        webbrowser.open("facebook.com")
    elif "send message" in query:
        send_message()
    elif "play song on youtube" in query or "play music on youtube" in query:
        play_song_on_youtube()
    elif "tell me a joke" in query or "make me laugh" in query:
        tell_joke()
    elif "shutdown" in query:
        shutdown()
    elif "restart" in query:
        restart()
    elif "sleep" in query:
        sleep()
    elif "weather" in query:
        get_weather()
    elif "set reminder" in query:
        set_reminder()
    elif "exit" in query:
        speak("Goodbye!")
        return False
    return True


def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def play_movie():
    movie_dir = "C:\\Users\\KIIT\\Downloads\\Video"
    movie = random.choice(os.listdir(movie_dir))
    os.startfile(os.path.join(movie_dir, movie))


def get_ip_address():
    try:
        ip = get('https://api.ipify.org').text
        speak(f"Your IP address is {ip}")
    except Exception as e:
        speak("Sorry, I couldn't fetch your IP address.")
        print(f"Error: {e}")


def search_wikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        print(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Your query is ambiguous. Please be more specific.")
        print(f"DisambiguationError: {e}")
    except wikipedia.exceptions.PageError as e:
        speak("The page does not exist.")
        print(f"PageError: {e}")
    except Exception as e:
        speak("Sorry, I couldn't fetch the information.")
        print(f"Error: {e}")


def search_youtube():
    speak("Astik, what should I search on YouTube?")
    query = take_command()
    if query != "none":
        encoded_query = quote(query)
        url = f"https://www.youtube.com/results?search_query={encoded_query}"
        webbrowser.open(url)


def search_google():
    speak("Astik, what should I search on Google?")
    query = take_command()
    if query != "none":
        encoded_query = quote(query)
        url = f"https://www.google.com/search?q={encoded_query}"
        webbrowser.open(url)


def send_message():
    speak("Who do you want to send a message to?")
    contact_name = take_command()
    if contact_name != "none":
        speak("What message do you want to send?")
        message = take_command()
        if message != "none":
            speak("I will send the message in one minute.")
            schedule_message(contact_name, message, 1)  # 1 minute delay


def play_song_on_youtube():
    speak("What song do you want to play on YouTube?")
    song_name = take_command()
    if song_name != "none":
        kit.playonyt(song_name)


def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)


def shutdown():
    speak("Shutting down the system.")
    os.system("shutdown /s /t 1")


def restart():
    speak("Restarting the system.")
    os.system("shutdown /r /t 1")


def sleep():
    speak("Putting the system to sleep.")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


def get_weather():
    speak("Fetching weather information...")
    city = "London"  # Default city, you can change it or add functionality to set it dynamically
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    try:
        response = get(weather_url)
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        speak(f"The current weather in {city} is {weather_desc} with a temperature of {temp} degrees Celsius.")
    except Exception as e:
        speak("Sorry, I couldn't fetch the weather information.")
        print(f"Error: {e}")


def set_reminder():
    speak("What should I remind you about?")
    reminder_text = take_command()
    if reminder_text != "none":
        speak("In how many minutes should I remind you?")
        delay_minutes = take_command()
        try:
            delay_minutes = int(delay_minutes)
            Timer(delay_minutes * 60, lambda: speak(f"Reminder: {reminder_text}")).start()
            speak(f"Reminder set for {delay_minutes} minutes from now.")
        except ValueError:
            speak("I couldn't understand the time. Please specify in minutes.")


def close_application(application_name):
    os.system(f"taskkill /f /im {application_name}")


if __name__ == "__main__":
    wish()
    while True:
        query = take_command()
        if query == "none":
            continue
        if not handle_query(query):
            break
