"""Example using the geocoding api"""

import httpx

from jetblack_open_meteo import prepare_geocoding_request


def main() -> None:
    url, params = prepare_geocoding_request("London")
    response = httpx.get(url, params=params)
    data = response.json()
    print(data)


if __name__ == '__main__':
    main()
