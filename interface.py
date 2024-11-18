"""
Interface module.
This module contains classes and functions to create a simple GUI to
show the weather of a city using the OpenWeatherMap API.
"""
import customtkinter
from PIL import Image
from api import get_current_weather, get_forecast, get_image


class WeatherApp():
    """Weather App class"""

    def __init__(self):

        self.image = Image.open("icons/sunny.jpg")
        # Creating main window

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root = customtkinter.CTk()
        self.root.geometry("700x650")
        self.root.title("Weather App")

        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=10, padx=15, fill="both", expand=True)

        # create and configure widgets
        label = customtkinter.CTkLabel(
            master=frame, text="Weather App", font=("Arial", 20))
        label.pack(pady=12, padx=10)

        # create a frame for the text entry
        text_frame = customtkinter.CTkFrame(master=frame)
        text_frame.pack(pady=6, padx=5, fill="x")

        label2 = customtkinter.CTkLabel(
            master=text_frame, text="Name of the City:", font=("Arial", 16))
        label2.pack(pady=1, padx=10)

        self.entry = customtkinter.CTkEntry(master=text_frame, width=150)
        self.entry.pack(pady=10, padx=10)

        button = customtkinter.CTkButton(
            master=text_frame, text="Get Weather", command=self.get_weather)
        button.pack(pady=10, padx=10)

        self.weather_frame = customtkinter.CTkFrame(master=frame)
        self.weather_frame.pack(pady=6, padx=5, fill="x")

        label3 = customtkinter.CTkLabel(
            master=self.weather_frame, text="Weather", font=("Arial", 16))
        label3.pack(pady=1, padx=10)

        # label for city
        self.label4 = customtkinter.CTkLabel(
            master=self.weather_frame, text="", font=("Arial", 16))
        self.label4.pack(pady=1, padx=10)
        # label for temperature
        self.label5 = customtkinter.CTkLabel(
            master=self.weather_frame, text="", font=("Arial", 16))
        self.label5.pack(pady=1, padx=10)
        # label for description
        self.label6 = customtkinter.CTkLabel(
            master=self.weather_frame, text="", font=("Arial", 16))
        self.label6.pack(pady=1, padx=10)
        # create an image
        self.ctk_image = customtkinter.CTkImage(
            light_image=self.image, dark_image=self.image, size=(200, 100))
        # create a label to display the image
        self.image_label = customtkinter.CTkLabel(
            master=self.weather_frame, image=self.ctk_image)
        self.image_label.pack(pady=1, padx=10)

    def generate_label(self, temp, desc, city_name):
        """Updates the labels with the data from the API"""

        # Update the text in the labels
        self.label4.configure(text=f"City: {city_name}")
        self.label5.configure(text=f"Temperature: {temp}ºC")
        self.label6.configure(text=f"Description: {desc}")

    def get_weather(self):
        """Calls the API to get the weather"""
        city_name = self.entry.get()
        if city_name:
            try:
                # Call the API for current weather
                result = get_current_weather(city_name.lower())
                # Call the API for forecast
                result_forecast = get_forecast(city_name.lower())
                # Get temperature, description and name
                temperature = result["main"]["temp"]
                description = result["weather"][0]["description"]
                name = result["name"]
                img = result["weather"][0]["icon"]
                # Call Generate label function
                self.generate_label(temperature, description, name)
                icon_image = get_image(img)
            except Exception as e:
                print(f"An error occurred: {e}")

    def run(self):
        """run the app"""
        self.root.mainloop()
