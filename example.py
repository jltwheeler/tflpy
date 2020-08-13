import os

from dotenv import load_dotenv

from tflpy import TflApi

load_dotenv()
app_key = os.getenv("APP_KEY")

tflapi = TflApi(app_key)

test = tflapi.get_accidents_by_year(2015)
print(test[0]["lat"], test[0]["lon"])
