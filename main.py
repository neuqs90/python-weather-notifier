import requests
from plyer import notification
from time import sleep

while True:
    api_key = "" # Your Api Key , Get At : https://www.weatherapi.com/
    city = "" # Your City Name

    try:
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}")
    
        if response.status_code == 200:
            
            data = response.json()

            City = data["location"]["name"]
            region = data["location"]["region"]
            tempc = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind_kmph = data["current"]["wind_kph"]
            cloud = data["current"]["cloud"]

            notification.notify(
                title="Weather",
                app_name="Weather",
                message=f"\nCity : {City}  Region : {region}\nCondition : {condition}\nTemperature C : {tempc}°\nHumidity : {humidity} %\nWind : {wind_kmph} Km/h\nCloud : {cloud} %",
                app_icon="weather.ico"
            )

            

        else:
            print(f"Request was not successful. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print("Exception Occured : ")

    sleep(7200) # Change Time Accordingly

# Github : github.com/neuqs90