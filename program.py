import requests
def Weather(CityName):
    key = "6f798521dfdf428eb7953911240411"
    url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={CityName}&aqi=no'
    try:
        response = requests.get(url).json()
        print(f"{CityName} is {response["current"]["temp_c"]}")
    except:
        print("We could not find the city name!")

CityName = input("Inter your city name: ")
Weather(CityName)
