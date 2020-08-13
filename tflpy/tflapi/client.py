"""
client
======

This module contains the primary wrapping class for interacting with the TfL
REST Api using the requests library.

"""

from typing import Dict, List, Union

import requests

from tflapi.exceptions import TflApiError


class TflApi:
    """Wrapper class for the TfL API"""

    def __init__(self, app_key: str = None) -> None:
        self.params: dict = {"app_key": app_key if app_key else None}
        self.base_url: str = "https://api.tfl.gov.uk/"

        self.init_resp = requests.get(self.base_url, params=self.params)
        if self.init_resp.status_code == 429:
            raise TflApiError("Please enter a valid app_key")

    def get_accidents_by_year(self, year: int) -> List[Dict]:
        url: str = f"{self.base_url}/AccidentStats/{year}"
        result = requests.get(url, params=self.params)

        if result.status_code != 200:
            raise TflApiError(result.json()["message"])

        return result.json()

    def get_air_quality(self) -> Dict:
        url: str = f"{self.base_url}/AirQuality"
        result = requests.get(url, params=self.params)

        if result.status_code == 200:
            return result.json()

        raise TflApiError("An unkown error occured")

    def get_bike_points(self) -> List[Dict]:
        url: str = f"{self.base_url}/BikePoint"
        result = requests.get(url, params=self.params)

        if result.status_code == 200:
            return result.json()

        raise TflApiError("An unkown error occured")

    def get_bike_point_by_id(self, id_: str) -> List[Dict]:
        url: str = f"{self.base_url}/BikePoint/{id_}"
        result = requests.get(url, params=self.params)

        if result.status_code != 200:
            raise TflApiError(result.json()["message"])

        return result.json()
