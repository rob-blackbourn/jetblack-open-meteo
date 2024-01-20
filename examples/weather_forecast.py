"""A forecast example"""

import httpx
import pandas as pd

from jetblack_open_meteo import prepare_weather_forecast_request


def main() -> None:
    url, params = prepare_weather_forecast_request(
        (51.50242846391432, -0.1423227420691731),
        hourly=['temperature_2m'],
    )
    response = httpx.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data['hourly'])
    print(df)


if __name__ == '__main__':
    main()
