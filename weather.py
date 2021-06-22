import requests

import os

from datetime import datetime

api_key='40de4ec8bf4ab287e90712ff9848e4d0'

location=input("Enter the city name: ")

c_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link=requests.get(c_api_link)

data=api_link.json()

Temperature=((data['main']['temp'])-273.15)

Tem="{:.2f}".format(Temperature)

Weather=data['weather'][0]['description']

Humidity=data['main']['humidity']

Wind_speed=data['wind']['speed']

date_time=datetime.now().strftime("%d %b %Y || %I:%M:%S %p")

print("--------------------------------------------------------------------------")

print("Weather stats for - {} || {}".format(location.upper(),date_time))

print("--------------------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C ".format(Temperature))

print ("Current weather desc  : ",Weather)

print ("Current Humidity      : ",Humidity, '%')

print ("Current wind speed    : ",Wind_speed ,'kmph')

T=str(Temperature)

W=str(Weather)

H=str(Humidity)

Ws=str(Wind_speed)

f=open("Result.txt",'w')

t="Current temperature is: "

h="Current Humidity      : "

w="Current weather desc  : "

ws="Current wind speed    : "

f.write("--------------------------------------------------------------------------")

f.write("\n")

f.write("Weather stats for - {} || {}".format(location.upper(),date_time))

f.write("\n")

f.write("--------------------------------------------------------------------------")

f.write("\n")

f.write(t+Tem +" deg C")

f.write("\n")

f.write(w+W)
    
f.write("\n")

f.write(h+H)
    
f.write("\n")
    
f.write(ws+Ws+" kmph")
    
f.write("\n")

f.close()
