import os

from dotenv import load_dotenv

from tflpy import TflApi, BaseMap
from tflpy.utils import create_geojson_feature_points


load_dotenv()
app_key = os.getenv("APP_KEY")

tflapi = TflApi(app_key)

bike_points = tflapi.get_bike_points()
data = [(bike_point["lon"], bike_point["lat"]) for bike_point in bike_points]
properties = [{"id": bike_point["id"]} for bike_point in bike_points]

bm = BaseMap()
bm.add_data(create_geojson_feature_points(data, properties))
bm.save_figure()
