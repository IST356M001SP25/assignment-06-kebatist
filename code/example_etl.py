import streamlit as st
import pandas as pd
import json 
from apicalls import get_weather, geocode


'''
This is a sample Multi-step data pipeline. 
Given a list of places it will provide the current weather conditions for each place.

steps:
    1. locations -> geocode -> location, lat, lon
    2. location, lat, lon -> weather -> location, lat, lonm temp, precip

RECALL: each step should input a file or dataframe and output a file AND dataframe
'''

# Define the cache files (outputs from the two steps)
LOCATION_SOURCE_FILE = "cache/locations.csv"
GEOCODE_CACHE_FILE = "cache/geocoded_locations.csv"
WEATHER_CACHE_FILE = "cache/weather_locations.csv"

def geocode_step(locations: str|pd.DataFrame) -> pd.DataFrame:
    '''
    1. locations -> geocode -> location, lat, lon
    '''

    # if string, then its a filename so load into dataframe
    if isinstance(locations, str):
        locations_dataframe = pd.read_csv(locations)
        # check if the file is empty
        if locations_dataframe.empty:
            raise ValueError(f"The file {locations} is empty. Please provide a valid file with location data.")
    else:
        locations_dataframe = locations

    # transformations 
    geocoded_data = []
    for idx, row in locations_dataframe.iterrows():
        geocode_result = geocode(row['location'])
        # extract what we need, this is a nested dictionary
        # the first result is the best result, so we take the first one
        latitude = geocode_result['results'][0]['geometry']['location']['lat']
        longitude = geocode_result['results'][0]['geometry']['location']['lng']
        # create item to add to list
        geocode_item = {'location': row['location'], 'lat': latitude, 'lon': longitude}
        # append to list, this is a list of dictionaries, each dictionary is a row in the dataframe
        geocoded_data.append(geocode_item)
    geocoded_locations_dataframe = pd.DataFrame(geocoded_data)

    # save to cache, return dataframe
    geocoded_locations_dataframe.to_csv(GEOCODE_CACHE_FILE, index=False, header=True)
    return geocoded_locations_dataframe

def weather_step(geocoded_locations: str|pd.DataFrame) -> pd.DataFrame:
    '''
    2. location, lat, lon -> weather -> location, temp, precip
    '''

    # if string, then its a filename so load into dataframe
    if isinstance(geocoded_locations, str):
        geocoded_locations_df = pd.read_csv(geocoded_locations)
    else:
        geocoded_locations_df = geocoded_locations

    # transformations 
    weather_locations = []
    for index, row in geocoded_locations_df.iterrows():
        #extract what we need
        weather = get_weather(row['lat'], row['lon'])
        temp = weather['current']['temperature_2m']
        precip = weather['current']['precipitation']
        # create item to add to list
        weather_item = {'location': row['location'], 'lat': row['lat'], 'lon' : row['lon'], 'temp': temp, 'precip': precip}
        weather_locations.append(weather_item)
    weather_locations_df = pd.DataFrame(weather_locations)

    # save to cache, return dataframe
    weather_locations_df.to_csv(WEATHER_CACHE_FILE, index=False, header=True)
    return weather_locations_df

if __name__ == '__main__':

    # This is one way to run the multi-step pipeline, with files
    geocode_step(LOCATION_SOURCE_FILE)
    weather_step(GEOCODE_CACHE_FILE)
    weather_locations = pd.read_csv(WEATHER_CACHE_FILE)
    print(weather_locations)

    # this is another way, using dataframes in memory
    locations = pd.read_csv(LOCATION_SOURCE_FILE)
    geocoded_locations = geocode_step(locations)
    weather_locations = weather_step(geocoded_locations)
    print(weather_locations)

