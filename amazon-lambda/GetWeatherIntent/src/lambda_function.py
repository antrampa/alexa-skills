# $ pip install requests
import boto3
import botocore
import json
#from botocore.vendored import requests
#import requests
import urllib3

#http = urllib3.PoolManager()
#r = http.request('GET', 'http://httpbin.org/robots.txt')


def get_weather():
    API_KEY = "<>"  # Replace with your API Key
    CITY = "Thessaloniki"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    #temp = "25"
    #description = "Chilly with increasing clouds"
    # return f"The current temperature in {CITY} is {temp}°C with {description}."
    #response = requests.get(url)
    #data = response.json()
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = response.data
    values = json.loads(data)
    #return values
    if response.status == 200:
        temp = values["main"]["temp"]
        description = values["weather"][0]["description"]
        return f"The current temperature in {CITY} is {temp}°C with {description}."
    else:
        return "Sorry, I couldn't fetch the weatherAAAA. " + response.status_code

def lambda_handler(event, context):
    # intent_name = event["request"]["intent"]["name"]
    
    # if intent_name == "GetWeatherIntent":
    #     speech_text = get_weather()
    # else:
    #     speech_text = "Sorry, I didn't understand that."
    
    speech_text = get_weather()
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": speech_text
            },
            "shouldEndSession": True
        }
    }
