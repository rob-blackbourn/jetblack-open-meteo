"""A forecast example"""

from datetime import date

import httpx
import pandas as pd

from jetblack_open_meteo import prepare_historical_weather_request


def main() -> None:
    url, params = prepare_historical_weather_request(
        (51.50242846391432, -0.1423227420691731),
        hourly=['temperature_2m'],
        start_date=date(2000, 1, 1),
        end_date=date.today()
    )
    response = httpx.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data['hourly'])
    print(df)


if __name__ == '__main__':
    main()
