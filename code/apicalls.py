import requests

# Put your CENT Ischool IoT Portal API KEY here.
APIKEY = "89b6dc8fb35ed9372acafa46"

def get_google_place_details(google_place_id: str) -> dict:
    '''
    Given a Google Place ID, return the place details.
    Written for example_etl.py

    Maybe, this should be in a separate file, but for now, I am keeping it here.
    # This function is used to get the details of a place from Google Places API.
    '''
    header = {'X-API-KEY: 89b6dc8fb35ed9372acafa46' }
    params = { 'place_id': google_place_id }
    url = f"https://cent.ischool-iot.net/api/google/places/details"
    response = requests.get(url=url, headers=header, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()
    
def get_azure_sentiment(text: str) -> dict:
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    data = { 'text': text }
    url = "https://cent.ischool-iot.net/api/azure/sentiment"
    response = requests.post(url=url, headers=header, data=data)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary
    # pass # Implement this function

'''
def get_azure_sentiment(text: str) -> dict:
    """
    Given a text input, return the sentiment analysis results from Azure API.
    """
    header = { 'X-API-KEY': APIKEY }  # Use the APIKEY variable for consistency
    data = { 'text': text }
    url = "https://new-api-path.net/api/azure/sentiment"  # Updated API path

    response = requests.post(url=url, headers=header, data=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()  # Return the JSON response as a dictionary
'''

def get_azure_key_phrase_extraction(text: str) -> dict:
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    data = { 'text': text }
    url = "https://cent.ischool-iot.net/api/azure/keyphrasextraction"
    response = requests.post(url=url, headers=header, data=data)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary
    #pass # Implement this function

def get_azure_named_entity_recognition(text: str) -> dict:
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    data = { 'text': text }
    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    response = requests.post(url=url, headers=header, data=data)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary
    pass # Implement this function


def geocode(place:str) -> dict:
    '''
    Given a place name, return the latitude and longitude of the place.
    Written for example_etl.py
    '''
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    params = { 'location': place }
    url = "https://cent.ischool-iot.net/api/google/geocode"
    response = requests.get(url=url, headers=header, params=params)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary


def get_weather(lat: float, lon: float) -> dict:
    '''
    Given a latitude and longitude, return the current weather at that location.
    written for example_etl.py
    '''
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    params = { 'lat': lat, 'lon': lon, 'units': 'imperial' }
    url = "https://cent.ischool-iot.net/api/weather/current"
    response = requests.get(url, headers=header, params=params)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary

if __name__ == '__main__':
    # Test the functions here if needed
    # Example: print(get_google_place_details('ChIJN1t_tDeuEmsRUsoyG83frY4'))
    pass  # Implement this function to test the API calls
    # Example: print(get_azure_sentiment('I love programming!'))

'''

import requests

# Put your CENT Ischool IoT Portal API KEY here.
APIKEY = "89b6dc8fb35ed9372acafa46"

# Define the base URL for the API
# The base URL is the common part of the URL for all API calls
# For example, if the API endpoint is "https://cent.ischool-iot.net/api/google/places/details",
# the base URL would be "https://cent.ischool-iot.net/api"
# This allows us to easily change the base URL if needed, without modifying each individual API call.
# The base URL is also used to construct the full URL for each API call by appending the specific endpoint to it.   
# This makes the code cleaner and easier to maintain.
# The base URL is also used to construct the full URL for each API call by appending the specific endpoint to it.
# This makes the code cleaner and easier to maintain.
# The base URL is also used to construct the full URL for each API call by appending the specific endpoint to it.

BASE_URL = "https://cent.ischool-iot.net/api"  # Base URL for all API calls

def make_request(method: str, endpoint: str, headers: dict, params=None, data=None) -> dict:
    """
    Helper function to make API requests.
    """
    url = f"{BASE_URL}/{endpoint}"
    response = requests.request(method, url, headers=headers, params=params, data=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def get_google_place_details(google_place_id: str) -> dict:
    """
    Given a Google Place ID, return the place details.
    """
    headers = {'X-API-KEY': APIKEY}
    params = {'place_id': google_place_id}
    return make_request("GET", "google/places/details", headers, params=params)

def get_azure_sentiment(text: str) -> dict:
    """
    Given a text input, return the sentiment analysis results from Azure API.
    """
    headers = {'X-API-KEY': APIKEY}
    data = {'text': text}
    return make_request("POST", "azure/sentiment", headers, data=data)

def get_azure_key_phrase_extraction(text: str) -> dict:
    """
    Given a text input, return the key phrase extraction results from Azure API.
    """
    headers = {'X-API-KEY': APIKEY}
    data = {'text': text}
    return make_request("POST", "azure/keyphrasextraction", headers, data=data)

def get_azure_named_entity_recognition(text: str) -> dict:
    """
    Given a text input, return the named entity recognition results from Azure API.
    """
    headers = {'X-API-KEY': APIKEY}
    data = {'text': text}
    return make_request("POST", "azure/entityrecognition", headers, data=data)

def geocode(place: str) -> dict:
    """
    Given a place name, return the latitude and longitude of the place.
    """
    headers = {'X-API-KEY': APIKEY}
    params = {'location': place}
    return make_request("GET", "google/geocode", headers, params=params)

# YES, I KNOW THIS IS A DUPLICATE FUNCTION, BUT I AM KEEPING IT FOR NOW
# TO AVOID BREAKING CHANGES IN THE EXAMPLE ETL FILES.

def get_weather(lat: float, lon: float) -> dict:
    """
    Given a latitude and longitude, return the current weather at that location.
    """
    headers = {'X-API-KEY': APIKEY}
    params = {'lat': lat, 'lon': lon, 'units': 'imperial'}
    return make_request("GET", "weather/current", headers, params=params)

if __name__ == '__main__':
    # Test the functions here if needed
    # Example: print(get_google_place_details('ChIJN1t_tDeuEmsRUsoyG83frY4'))
    pass
'''