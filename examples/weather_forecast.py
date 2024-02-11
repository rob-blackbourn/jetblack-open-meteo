"""A forecast example"""

import httpx
import pandas as pd
import requests

from jetblack_open_meteo.weather_forecast import (
    prepare_weather_forecast_request,
)


def weather_forecast_httpx() -> None:
    url, params = prepare_weather_forecast_request(
        (51.50242846391432, -0.1423227420691731),
        hourly=['temperature_2m'],
    )
    response = httpx.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data['hourly'])
    print(df)


def weather_forecast_requests() -> None:
    url, params = prepare_weather_forecast_request(
        (51.50242846391432, -0.1423227420691731),
        hourly=['temperature_2m'],
    )
    response = requests.get(url, params=params, timeout=600)
    data = response.json()
    df = pd.DataFrame(data['hourly'])
    print(df)


if __name__ == '__main__':
    # weather_forecast_httpx()
    weather_forecast_requests()
