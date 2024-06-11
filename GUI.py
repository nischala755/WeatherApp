import tkinter as tk
from tkinter import messagebox
from plot_forecast import plot_forecast  # Import the plot_forecast function


def fetch_forecast():
    city = city_entry.get()
    api_key = "YRH6NFL2X3D9AABUD5UQ6R9QV"  # Replace with your actual Visual Crossing API key

    import io
    import contextlib

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        plot_forecast(city, api_key)

    forecast_result = output.getvalue()
    output.close()

    forecast_text.config(state=tk.NORMAL)
    forecast_text.delete(1.0, tk.END)
    forecast_text.insert(tk.END, forecast_result)
    forecast_text.config(state=tk.DISABLED)


# Create GUI window
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter city name:").pack()
city_entry = tk.Entry(root)
city_entry.pack()
tk.Button(root, text="Get Weather Forecast", command=fetch_forecast).pack()
tk.Button(root, text="Plot Weather Forecast",
          command=lambda: plot_forecast(city_entry.get(), "YOUR_VISUAL_CROSSING_API_KEY")).pack()

forecast_text = tk.Text(root, state=tk.DISABLED, width=80, height=20)
forecast_text.pack()

root.mainloop()
