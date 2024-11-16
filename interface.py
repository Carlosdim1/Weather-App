"""
Interface module.
This module contains classes and functions to create a simple GUI to
show the weather of a city using the OpenWeatherMap API.
"""
import customtkinter


class WeatherApp():
    """Weather App class"""

    def __init__(self):
        # Creating main window

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root = customtkinter.CTk()
        self.root.geometry("700x650")
        self.root.title("Weather App")

        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=10, padx=15, fill="both", expand=True)

        # Crear y configurar los widgets
        label = customtkinter.CTkLabel(
            master=frame, text="Weather App", font=("Arial", 20))
        label.pack(pady=12, padx=10)

        # Crear un marco para campos de texto
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

    def get_weather(self):
        """Calls the API to get the weather"""
        city_name = self.entry.get()
        if city_name:
            # Call the API
            print(f"Getting weather for {city_name}")
            # Call Generate label function
            self.generate_label(city_name)

    def generate_label(self, text):
        """Generates a label with the given text inside weather_frame"""

        label = customtkinter.CTkLabel(
            master=self.weather_frame, text=text, font=("Arial", 16))
        label.pack(pady=1, padx=10)

    def run(self):
        """run the app"""
        self.root.mainloop()
