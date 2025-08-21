# By Daniyal

import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io
from dotenv import load_dotenv
load_dotenv()
import os


# Function to Get  weather data
def get_weather():
    city = city_entry.get()
    api_key = os.getenv("api_key")  # Api key in .env file
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            location = f"{data['location']['name']}, {data['location']['region']}, {data['location']['country']}"
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            cloud = data['current']['cloud']
            wind_speed = data['current']['wind_kph']

            # Get the icon image part
            icon_url = f"http:{data['current']['condition']['icon']}"
            icon_response = requests.get(icon_url)
            icon_image = Image.open(io.BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image)

            weather_label.config(text=f"\nLocation: {location}\nTemperature: {temperature}°C\nCondition: {condition}\nHumidity: {humidity}%\nCloud Cover: {cloud}\nWind-Speed: {wind_speed}kph")
            
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo
        else:
            messagebox.showerror("Error", data.get("error", {}).get("message", "Unable to get weather data"))
    except Exception as e:
        messagebox.showerror("Error", "Unable to get weather data")

# TKinter GUI
root = tk.Tk()
root.title("Weather App (By Daniyal)")
root.geometry("350x300") # width x height

city_label = tk.Label(root, text="City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_button = tk.Button(root, text="Get Weather", command=get_weather)
get_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

icon_label = tk.Label(root)
icon_label.pack()

made_by_label = tk.Label(root, text="Made by Daniyal Rashid", font=("Helvetica", 10))
made_by_label.pack(side=tk.BOTTOM, pady=5)

# Run the application
root.mainloop()