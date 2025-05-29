import json
from utils.fetch_weather import get_weather_data

def read_cities(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_data(data, filename='weather_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def generate_report(data):
    temperatures = []
    clear_cities = []

    for entry in data:
        try:
            temp = entry['current']['temp_c']
            desc = entry['current']['condition']['text']
            city = entry['location']['name']
            temperatures.append((city, temp))

            # Debug print
            print(f"{city}: {temp}°C, {desc}")

            if 'clear' in desc.lower() or 'sunny' in desc.lower():
                clear_cities.append(city)

        except KeyError as e:
            print(f"Missing expected data for an entry: {e}")
            continue

    if not temperatures:
        print("No valid weather data to generate report.")
        return

    highest = max(temperatures, key=lambda x: x[1])
    lowest = min(temperatures, key=lambda x: x[1])
    avg_temp = sum(t[1] for t in temperatures) / len(temperatures)

    degree = "\u00B0"  # Unicode for °
    report = f"""Weather Summary Report
Cities Processed: {len(data)}

Highest Temperature: {highest[1]}{degree}C - {highest[0]}
Lowest Temperature: {lowest[1]}{degree}C - {lowest[0]}
Average Temperature: {round(avg_temp, 1)}{degree}C

Clear Weather Cities: {len(clear_cities)}
{chr(10).join(['- ' + city for city in clear_cities])}
"""

    with open('summary_report.txt', 'w') as f:
        f.write(report)

def main():
    cities = read_cities('cities.txt')
    weather_data = []

    for city in cities:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)
        else:
            print(f"Failed to fetch data for {city}")

    save_data(weather_data)
    generate_report(weather_data)

if __name__ == '__main__':
    main()
