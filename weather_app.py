import requests

def get_forecast(city, api_key):
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    complete_url = f"{base_url}{city}?key={api_key}&unitGroup=metric&include=days&elements=datetime,temp,conditions"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()

        # Print the full response for debugging
        print(f"Full API response: {data}")

        if 'days' in data:
            print(f"\n5-Day Weather Forecast for {city}:\n")
            for forecast in data['days']:
                date = forecast['datetime']
                temp = forecast['temp']
                condition = forecast['conditions']
                print(f"{date} - Temperature: {temp}°C, Conditions: {condition}")
        else:
            print(f"Error: {data.get('message', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fetch weather data for a given city.")
    parser.add_argument("city", type=str, help="Name of the city")
    parser.add_argument("api_key", type=str, help="Visual Crossing API key")

    args = parser.parse_args()

    get_forecast(args.city, args.api_key)
