# By Daniyal

import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io
from dotenv import load_dotenv
load_dotenv()
import os


# Function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    api_key = os.getenv("api_key")  # Api key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            location = f"{data['location']['name']}, {data['location']['region']}, {data["location"]["country"]}"
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            cloud = data['current']['cloud']
            wind_speed = data['current']['wind_kph']

            # Get the icon image part
            icon_url = f"http:{data["current"]["condition"]["icon"]}"
            icon_response = requests.get(icon_url)
            icon_image = Image.open(io.BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image)

            weather_label.config(text=f"\nLocation: {location}\nTemperature: {temperature}°C\nCondition: {condition}\nHumidity: {humidity}%\nCloud Cover: {cloud}\nWind-Speed: {wind_speed}kph")
            
            # Display the icon
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo
        else:
            messagebox.showerror("Error", data.get("error", {}).get("message", "Unable to fetch weather data"))
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")

# Set up the GUI
root = tk.Tk()
root.title("Weather App (By Daniyal)")
root.geometry("350x300") # width x height

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

icon_label = tk.Label(root)
icon_label.pack()

made_by_label = tk.Label(root, text="Made by Daniyal Rashid", font=("Helvetica", 10))
made_by_label.pack(side=tk.BOTTOM, pady=5)

# Run the application
root.mainloop()


# Documantation of Api:
# {'location': {'name': 'Gujranwala', 'region': 'Punjab', 'country': 'Pakistan', 'lat': 32.15, 'lon': 74.1833, 'tz_id': 'Asia/Karachi', 'localtime_epoch': 1731781939, 'localtime': '2024-11-16 23:32'}, 'current':o {'last_updated_epoch': 1731781800, 'last_updated': '2024-11-16 23:30', 'temp_c': 20.1, 'temp_f': 68.2, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', '0code': 1000}, 'wind_mph': 7.6, 'wind_kph': 12.2, 'wind_degree': 358, 'wind_dir': 'N', 'pressure_mb': 1014.0, 'pressure_in': 29.93, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 45, 'cloud': 6, 'feelslike_c':, 20.1, 'feelslike_f': 68.2, 'windchill_c': 20.1, 'windchill_f': 68.2, 'heatindex_c': 20.1, 'heatindex_f': 68.2, 'dewpoint_c': 8.0, 'dewpoint_f': 46.3, 'vis_km': 10.0, 'vis_miles': 6.0, 'uv': 0.0, 'gust_mph': 15.5, 'gust_kph': 24.9}}