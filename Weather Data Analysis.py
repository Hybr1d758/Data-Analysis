import requests
import csv
import datetime

url = "https://api.openweathermap.org/data/3.0/onecall?lat=1.2350&lon=54.5742&exclude=hourly,minutely,alerts&appid=8300f423a4380bc2e5512b4a6c8db417"

params = {
    "latitude":1.2350,
    "longitude":54.5742,
    "timezone": "Europe/London",
    "current":"dt,pressure, humidity, wind_speed,dew_point"
} 


location = input("whats your location? ")
lat = input("Enter your latitude:")
lon = input("Enter your longitude:")



#function to make a request to the weather API

def weather(location):
        params = {
            }
        url="https://api.openweathermap.org/data/3.0/onecall?"+lat+"&"+lon+"&exclude=hourly,minutely,alerts&appid=8300f423a4380bc2e5512b4a6c8db417"
        response =requests.get(url,params=params)
        return response

response = requests.get(url,params=params)
print(response.status_code)
#print(f"data:{response.json()}")
data = response.json()
daily_data = data.get("daily")
#print("Daily data: ",daily_data)


#function to convert unix time to datetime string

def timestamp(unix_time):
    dt = datetime.datetime.utcfromtimestamp(unix_time)
    dt_string = dt.strftime("%Y-%m-%d %H:%M:%S")
    return(dt_string)


datetime_string = [timestamp(date_time["dt"]) for date_time in daily_data]

print("Datetime_string:",datetime_string)



daily_dt = datetime_string
daily_pressure = [psi["pressure"] for psi in daily_data]
daily_humidity = [moist["humidity"] for moist in daily_data]
daily_wind_speed = [air["wind_speed"] for air in daily_data]
daily_dew_point = [dew["dew_point"] for dew in daily_data]
#print(daily_dt)
#print(daily_pressure)
#print(daily_humidity)
#print(daily_wind_speed)
#print(daily_dew_point)

headers = ["datetime","pressure","humidity","windspeed","dewpoint"]

data_dict = {}

for e in range(len(daily_data)):
    datetime = daily_dt[e]
    pressure = daily_pressure[e]
    humidity = daily_humidity[e]
    windspeed = daily_wind_speed[e]
    dewpoint = daily_dew_point[e]
    data_dict[datetime] = f"{pressure},{humidity},{windspeed}{dewpoint}"

print(data_dict)

csv_file = 'data_dict.csv'

data_dict = ([1],[2],[3],[4])

with open(csv_file, 'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_dict)
