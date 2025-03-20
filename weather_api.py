import requests
import pyttsx3

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Unable to fetch weather data.")
        return None

def speak_weather(weather_data):
    if not weather_data:
        return

    city = weather_data['name']
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    speech_text = f"The current weather in {city} is {temp} degrees Celsius with {description}."
    
    print(speech_text)  
    engine = pyttsx3.init()
    engine.say(speech_text)
    engine.runAndWait()

if _name_ == "_main_":
    api_key = "62ea1d21635668c35addf4e76bc76235"  
    city = input("Enter your city: ")
    
    weather_data = get_weather(city, api_key)
    speak_weather(weather_data)