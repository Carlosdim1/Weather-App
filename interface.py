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

        weather_frame = customtkinter.CTkFrame(master=frame)
        weather_frame.pack(pady=6, padx=5, fill="x")

    def get_weather(self):
        """Calls the API to get the weather"""
        pass

    def run(self):
        """run the app"""
        self.root.mainloop()
