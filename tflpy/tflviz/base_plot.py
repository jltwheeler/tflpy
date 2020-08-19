import os
import json
from typing import Tuple

from bokeh.io import output_file, save  # type: ignore
from bokeh.models import GeoJSONDataSource  # type: ignore
from bokeh.plotting import figure  # type: ignore


class BaseMap:
    def __init__(self):
        boroughs_path = os.path.join(
            os.path.dirname(__file__), "data", "london_boroughs.json"
        )

        output_file("output.html")
        boroughs_geo = self._load_geo_json(boroughs_path)

        self.tooltips = [("Borough", "@name")]

        self.figure = figure(
            background_fill_color="lightblue",
            tooltips=self.tooltips,
            plot_width=1800,
            plot_height=850,
        )
        self.figure.patches(
            "xs",
            "ys",
            fill_color="white",
            line_color="black",
            source=boroughs_geo,
        )

    def _load_geo_json(self, geojson_path: str):
        with open(geojson_path, "rb") as json_file:
            data = json.load(json_file)

        return GeoJSONDataSource(geojson=json.dumps(data))

    def save_figure(self):
        save(self.figure)

    def add_data(self, geojson, tooltips: Tuple[str] = None):
        self.figure.circle(
            x="x", y="y", size=5, color="red", alpha=0.7, source=geojson
        )
