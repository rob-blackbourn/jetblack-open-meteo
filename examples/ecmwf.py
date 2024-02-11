"""A forecast example"""

from typing import TypedDict

import httpx

from jetblack_open_meteo.weather_forecast import (
    prepare_ecmwf_request
)


class CityDict(TypedDict):
    country: str
    city: str
    population: int
    latitude: float
    longitude: float


CITIES: list[CityDict] = [
    # {
    #     "country": "GB",
    #     "city": "London",
    #     "population": 8961989,
    #     "latitude": 51.508530,
    #     "longitude": -0.125740
    # },
    # {
    #     "country": "GB",
    #     "city": "Birmingham",
    #     "population": 1144919,
    #     "latitude": 52.481420,
    #     "longitude": -1.899830
    # },
    # {
    #     "country": "GB",
    #     "city": "Liverpool",
    #     "population": 864122,
    #     "latitude": 53.410580,
    #     "longitude": -2.977940
    # },
    # {
    #     "country": "GB",
    #     "city": "Glasgow",
    #     "population": 626410,
    #     "latitude": 55.865150,
    #     "longitude": -4.257630
    # },
    # {
    #     "country": "GB",
    #     "city": "Sheffield",
    #     "population": 556500,
    #     "latitude": 53.382970,
    #     "longitude": -1.465900
    # },
    # {
    #     "country": "GB",
    #     "city": "Leeds",
    #     "population": 516298,
    #     "latitude": 53.796480,
    #     "longitude": -1.547850
    # },
    # {
    #     "country": "GB",
    #     "city": "Edinburgh",
    #     "population": 506520,
    #     "latitude": 55.952060,
    #     "longitude": -3.196480
    # },
    # {
    #     "country": "GB",
    #     "city": "Bristol",
    #     "population": 465866,
    #     "latitude": 51.455230,
    #     "longitude": -2.596650
    # },
    # {
    #     "country": "GB",
    #     "city": "Cardiff",
    #     "population": 447287,
    #     "latitude": 51.480000,
    #     "longitude": -3.180000
    # },
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
    # {
    #     "country": "GB",
    #     "city": "Leicester",
    #     "population": 368600,
    #     "latitude": 52.638600,
    #     "longitude": -1.131690
    # },
    # {
    #     "country": "GB",
    #     "city": "Bradford",
    #     "population": 366187,
    #     "latitude": 53.793910,
    #     "longitude": -1.752060
    # }
]


def tocoord(value: float) -> float:
    times_ten = round(value * 10, 0)
    to_fours = round(times_ten / 4) * 4
    return round(to_fours / 10, 1)


def ecmwf() -> None:
    coordinates = [
        (city['latitude'], city['longitude'])
        for city in CITIES
    ]
    url, params = prepare_ecmwf_request(
        coordinates,
        hourly=['temperature_2m'],
    )
    response = httpx.get(url, params=params)
    data = response.json()
    print(data)
    # with open('cities-ecwmf.json', 'w', encoding='utf8') as fp:
    #     fp.write(response.text)


if __name__ == '__main__':
    ecmwf()
