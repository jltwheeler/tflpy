from typing import List, Dict

from geojson import Feature, FeatureCollection, Point, dumps  # type: ignore
from bokeh.models import GeoJSONDataSource  # type: ignore


def create_geojson_feature_points(
    data: List[float], properties_list: List[Dict[str, str]]
):
    collection = []
    for point, properties in zip(data, properties_list):
        collection.append(
            Feature(geometry=Point(point), properties=properties)
        )

    feature_collection = FeatureCollection(collection)

    return GeoJSONDataSource(geojson=dumps(feature_collection))
