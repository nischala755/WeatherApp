import matplotlib.pyplot as plt
from weather_app import get_forecast


def plot_forecast(city, api_key):
    import io
    import contextlib
    import json

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        get_forecast(city, api_key)

    forecast_result = output.getvalue()
    output.close()

    # Parse the JSON data
    data = json.loads(forecast_result)
    if 'days' not in data:
        print("Error in data:", data)
        return

    dates = [day['datetime'] for day in data['days']]
    temps = [day['temp'] for day in data['days']]

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker='o')
    plt.title(f'5-Day Temperature Forecast for {city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Plot weather forecast for a given city.")
    parser.add_argument("city", type=str, help="Name of the city")
    parser.add_argument("api_key", type=str, help="Visual Crossing API key")

    args = parser.parse_args()

    plot_forecast(args.city, args.api_key)
