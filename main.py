"""Main module for the Weather App.
This module contains the main function that runs the WeatherApp."""
from interface import WeatherApp


def main():
    """Main function that Runs the WeatherApp """
    app = WeatherApp()
    app.run()


if __name__ == "__main__":
    main()
