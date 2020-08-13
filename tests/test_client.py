import os

import pytest
from dotenv import load_dotenv

from tflapi import TflApi
from tflapi.exceptions import TflApiError

load_dotenv()
app_key = os.getenv("APP_KEY")


def test_valid_app_key():
    tflapi = TflApi()
    assert tflapi.init_resp.status_code == 200


def test_invalid_app_key():
    with pytest.raises(TflApiError):
        TflApi("invalidkey")


def test_get_accidents_by_year():
    tflapi = TflApi(app_key)

    assert len(tflapi.get_accidents_by_year(2018)) > 0


def test_get_accidents_by_year_error():
    tflapi = TflApi(app_key)

    with pytest.raises(TflApiError):
        tflapi.get_accidents_by_year(2500)


def test_get_air_quality():
    tflapi = TflApi(app_key)

    assert len(tflapi.get_air_quality()) > 0


def test_get_bike_points():
    tflapi = TflApi(app_key)

    assert len(tflapi.get_bike_points()) > 0


def test_get_bike_point_by_id():
    tflapi = TflApi(app_key)

    assert len(tflapi.get_bike_point_by_id("BikePoints_1")) > 0


def test_get_bike_point_by_id_error():
    tflapi = TflApi(app_key)

    with pytest.raises(TflApiError):
        tflapi.get_bike_point_by_id(2)
