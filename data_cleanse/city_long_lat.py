import requests
import json
from config import google_places_key
import pandas as pd
import os

if not os.path.exists('../Resources/manuel/map_information'):
    data = pd.read_csv('../Resources/manuel/glassdoor_data_scientist_jobs.csv')
    sorted_cities = data["Location"].unique()

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    cities = []
    state = []
    long = []
    lat = []
    for x in sorted_cities:
        state.append(x[-2:])
        cities.append(x[:-4])
        payload = requests.get(f'{url}{str(x).replace(" ", "+")}&key={google_places_key}').json()
        long.append(payload['results'][0]['geometry']['location']['lng'])
        lat.append(payload['results'][0]['geometry']['location']['lat'])
        print(f'{x} added!')

    map_info = pd.DataFrame({
        "city": cities,
        "state": state,
        "long": long,
        "lat": lat
    })
    map_info.to_csv("Resources/map_information", index=False)
data = pd.read_csv('../Resources/manuel/map_information')

