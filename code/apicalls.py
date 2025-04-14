import requests

# Put your CENT Ischool IoT Portal API KEY here.
APIKEY = "89b6dc8fb35ed9372acafa46"

def get_google_place_details(google_place_id: str) -> dict:
    '''
    Given a Google Place ID, return the place details.
    Written for example_etl.py
    '''
    header = "89b6dc8fb35ed9372acafa46"
    params = { 'place_id': google_place_id }
    url = f"https://cent.ischool-iot.net/api/google/places/details"{google_place_id}&key="89b6dc8fb35ed9372acafa46"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()
    
def get_azure_sentiment(text: str) -> dict:
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    data = { 'text': text }
    url = "https://cent.ischool-iot.net/api/azure/sentiment"
    response = requests.post(url, headers=header, data=data)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary
    # pass # Implement this function

def get_azure_key_phrase_extraction(text: str) -> dict:
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    data = { 'text': text }
    url = "https://cent.ischool-iot.net/api/azure/keyphrasextraction"
    response = requests.post(url, headers=header, data=data)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary
    #pass # Implement this function

def get_azure_named_entity_recognition(text: str) -> dict:
    header = { 'X-API-KEY': "89b6dc8fb35ed9372acafa46" }
    data = { 'text': text }
    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    response = requests.post(url, headers=header, data=data)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary
    pass # Implement this function


def geocode(place:str) -> dict:
    '''
    Given a place name, return the latitude and longitude of the place.
    Written for example_etl.py
    '''
    header = { 'X-API-KEY': APIKEY }
    params = { 'location': place }
    url = "https://cent.ischool-iot.net/api/google/geocode"
    response = requests.get(url, headers=header, params=params)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary


def get_weather(lat: float, lon: float) -> dict:
    '''
    Given a latitude and longitude, return the current weather at that location.
    written for example_etl.py
    '''
    header = { 'X-API-KEY': APIKEY }
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