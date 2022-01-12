import requests
import os

def get_weather_desc_and_temp():
    os.environ["9653138eba7d8f14a8ac897d2c1a60f1"] = "1"
    api_key = str(os.environ["9653138eba7d8f14a8ac897d2c1a60f1"])

    city = "Valdez"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()
    print(json)

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
                'temp_min': temp_min,
                'temp_max': temp_max}

def main():
    # Print the results
    weather_dict = get_weather_desc_and_temp()
    print("Today's forcast is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The maximum temperature is", weather_dict.get('temp_max'))

main()
