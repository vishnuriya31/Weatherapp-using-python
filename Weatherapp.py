import tkinter as tk
import requests

def get_weather():
    city = city_entry.get().strip()
    if not city:
        weather_label.config(text="Please enter a city name.")
        return

    # Construct the URL to request weather in JSON format
    url = f"http://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        data = response.json()
        
        # Extract current weather information
        current = data["current_condition"][0]
        temp = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        description = current["weatherDesc"][0]["value"]

        weather_info = (
            f"City: {city}\n"
            f"Temperature: {temp}°C\n"
            f"Feels Like: {feels_like}°C\n"
            f"Condition: {description}"
        )
        weather_label.config(text=weather_info)
    except Exception as e:
        weather_label.config(text="Error retrieving weather data.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# City input label and entry
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=(10, 0))

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Button to trigger weather fetching
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Label to display weather information
weather_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
weather_label.pack(pady=(10, 20))

# Run the application
root.mainloop()
