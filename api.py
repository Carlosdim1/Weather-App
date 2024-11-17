import requests
from config import API_KEY, BASE_URL


def build_url(endpoint, params) -> str:
    """Build URL to make an API request."""
    params['appid'] = API_KEY  # Agrega la clave de API
    # endpoint is the final segment of the URL (weather, forecast, etc.)
    # params is a dictionary of query parameters (city, units, etc.)
    # requests.compat.urlencode() converts the dictionary to a URL-encoded string
    # example, from: params = {"q": "Madrid", "units": "metric", "appid": API_KEY}
    # to: params = "q=Madrid&units=metric&appid=API_KEY"
    # final url = https://api.openweathermap.org/data/2.5/weather?q=Madrid&units=metric&appid=API_KEY
    return f"{BASE_URL}{endpoint}?{requests.compat.urlencode(params)}"


def make_request(url):
    """Make an HTTP request and return the data."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if the request was successful (200 OK)
        return response.json()  # Return the JSON data
    except requests.exceptions.HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_current_weather(city):
    """Get the current weather for a city."""
    # units = metric for celsius
    url = build_url("weather", {"q": city, "units": "metric"})
    return make_request(url)


def get_forecast(city):
    """Get the forecast for a city."""
    # q = city as a query parameter
    url = build_url("forecast", {"q": city, "units": "metric"})
    return make_request(url)


# Example usage
"""
if __name__ == "__main__":
    # In Python, constants are typically written in all uppercase
    # letters with underscores separating words, as per PEP 8 style guide
    CITY = "Valencia"
    print(get_current_weather(CITY))
    print(get_forecast(CITY))
"""
