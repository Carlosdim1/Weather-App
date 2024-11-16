from config import API_KEY, BASE_URL

import requests


def build_url(endpoint: str, params: dict) -> str:
    """Construye la URL completa para las llamadas a la API."""
    params['appid'] = API_KEY  # Agrega la clave de API
    return f"{BASE_URL}{endpoint}?{requests.compat.urlencode(params)}"
