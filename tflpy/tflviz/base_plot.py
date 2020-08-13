import os
import json

from bokeh.io import output_file, save
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure


class BaseMap:
    def __init__(self):
        output_file("geojson.html")

        with open(
            os.path.join(
                os.path.dirname(__file__), "data", "london_boroughs.json"
            ),
            "rb",
        ) as json_file:
            data = json.load(json_file)

        geo_source = GeoJSONDataSource(geojson=json.dumps(data))

        tooltips = [("Name", "@name")]

        p = figure(
            background_fill_color="lightgrey",
            tooltips=tooltips,
            match_aspect=True,
        )
        p.patches(
            "xs",
            "ys",
            fill_color="white",
            line_color="black",
            source=geo_source,
        )

        save(p)
