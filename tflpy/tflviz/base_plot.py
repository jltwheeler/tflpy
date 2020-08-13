import os
import json

from bokeh.io import output_file, save
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure


class BaseMap:
    def __init__(self):
        output_file("geojson.html")

        with open(
            os.path.join(os.getcwd(), "data/london_boroughs.json"), "rb"
        ) as f:
            data = json.load(f)

        geo_source = GeoJSONDataSource(geojson=json.dumps(data))

        TOOLTIPS = [("Name", "@name")]

        p = figure(
            background_fill_color="lightgrey",
            tooltips=TOOLTIPS,
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
