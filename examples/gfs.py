"""A forecast example"""

from typing import TypedDict

import httpx

from jetblack_open_meteo.weather_forecast import (
    prepare_gfs_request
)


class CityDict(TypedDict):
    country: str
    city: str
    population: int
    latitude: float
    longitude: float


CITIES: list[CityDict] = [
    {
        "country": "GB",
        "city": "Manchester",
        "population": 395515,
        "latitude": 53.480950,
        "longitude": -2.237430
    },
    {
        "country": "GB",
        "city": "Manchester2",
        "population": 395515,
        "latitude": 53.6,
        "longitude": -2.4
    },
]


def tocoord(value: float) -> float:
    times_ten = round(value * 10, 0)
    to_fours = round(times_ten / 4) * 4
    return round(to_fours / 10, 1)


def gfs() -> None:
    coordinates = [
        (city['latitude'], city['longitude'])
        for city in CITIES
    ]
    url, params = prepare_gfs_request(
        coordinates,
        hourly=['temperature_2m'],
    )
    response = httpx.get(url, params=params)
    data = response.json()
    print(data)
    # with open('cities-ecwmf.json', 'w', encoding='utf8') as fp:
    #     fp.write(response.text)


if __name__ == '__main__':
    gfs()
