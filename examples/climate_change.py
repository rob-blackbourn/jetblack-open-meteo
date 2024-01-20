"""A climate change example"""

from datetime import date, timedelta

import httpx
import pandas as pd

from jetblack_open_meteo import prepare_climate_change_request


def main() -> None:
    start_date = date.today()
    end_date = start_date + timedelta(days=365)

    url, params = prepare_climate_change_request(
        (51.50242846391432, -0.1423227420691731),
        daily=['temperature_2m_mean'],
        start_date=start_date,
        end_date=end_date
    )
    response = httpx.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data['daily'])
    print(df)


if __name__ == '__main__':
    main()
