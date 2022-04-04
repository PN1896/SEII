from urllib import request
import requests,json

location_search = "location/search/"
location= "location/"
#Aufgabe 1.1
url_api = "https://www.metaweather.com/api/"
params = {"query": "Hanover"}

response =requests.get(url_api + location_search,params)

json = response.json()

print("respondcode:", response)
print("respond json:", response.json())
print("response woeid: ", json[0]["woeid"])
#Aufgabe 1.2

woeid = json[0]["woeid"]
response_weather_han = requests.get(url_api+location+ str(woeid))
print("response_weather_H code:", response_weather_han.status_code)
print("response_weather_H json:", response_weather_han.json())
#print("response_weather_H  woeid: ", response_weather_han[0]["woeid"])
print(response_weather_han.json())


response_water_han_March = requests.get(url_api+ location +str(woeid)+"/2019/3/8")
print("response weather hann march 2019:", response_water_han_March.json())
