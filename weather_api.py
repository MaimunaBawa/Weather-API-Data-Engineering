import requests
import json
import pandas as pd

# requesting  data for Minais Gerais (Lat:-21.72, long: -45.39) from 01-01-2022 to 12-31-2023
# data being pulled are temperture, relative humidity, precipitation , & surface pressure.

URL="https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.47&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"

weather_api = URL
response = requests.get(weather_api)
data = response.json()


#Read and write JSON files using the 'with open()' statement and the 'json' module.
with open("data/json/weather_api.json", mode = "w") as file:
# convert list oject to json
    json.dump(data,file, indent = 4)

   
# Add json data file into data frame

df = pd.DataFrame(data)

#create new dict containing time, temperature,relative_humidity,precipitation,surface_pressure
hourly_data = data["hourly"]

new_dict = {
"time": hourly_data ["time"],
"temperature_2m": hourly_data["temperature_2m"],
"relative_humidity_2m": hourly_data["relative_humidity_2m"],
"precipitation": hourly_data ["precipitation"],
"surface_pressure": hourly_data ["surface_pressure"],
}
#Add new_dict into data frame
df=pd.DataFrame(new_dict)

#convert json file into a csv file,save csv to path

df.to_csv("data/csv/new.csv",index = False)

#Go through the data and find null
null_counts = df.isnull().sum()








           