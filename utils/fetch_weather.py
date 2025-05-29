import requests

API_KEY = '065c78c5a2d24f35b08141258252905'  # Replace with your actual API key
BASE_URL = 'https://api.weatherapi.com/v1/current.json'

def get_weather_data(city):
    url = f"{BASE_URL}?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.text}")
        return None