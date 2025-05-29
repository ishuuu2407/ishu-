# Weather Analysis & Report Generation

## Description
A Python CLI tool that:
- Fetches weather data for a list of cities
- Saves the data locally
- Analyzes and generates a weather report

## How to Run
1. Add cities to `cities.txt`
2. Replace `YOUR_API_KEY` in `fetch_weather.py` with your actual OpenWeatherMap API key.
3. Run the script:
   ```bash
   python main.py
   ```

## Requirements
- Python 3.6+
- requests
- matplotlib (optional)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Assumptions
- All cities are valid or handled gracefully
