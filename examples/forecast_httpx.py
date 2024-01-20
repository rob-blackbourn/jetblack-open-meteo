"""A forecast example"""

import httpx

from jetblack_open_meteo.weather_forecast import prepare_weather_forecast_request


def main() -> None:
    url, params = prepare_weather_forecast_request(
        (51.50242846391432, -0.1423227420691731),
        hourly=['temperature_2m']
    )
    response = httpx.get(url, params=params)
    data = response.json()
    print(data)


if __name__ == '__main__':
    main()
